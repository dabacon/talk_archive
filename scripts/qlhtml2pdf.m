#import <Cocoa/Cocoa.h>
#import <WebKit/WebKit.h>
#import <Quartz/Quartz.h>

@interface LoaderDelegate : NSObject <WebFrameLoadDelegate>
@property (nonatomic, assign) BOOL done;
@end

@implementation LoaderDelegate
- (void)webView:(WebView *)sender didFinishLoadForFrame:(WebFrame *)frame {
    if (frame == [sender mainFrame]) {
        self.done = YES;
    }
}
- (void)webView:(WebView *)sender didFailLoadWithError:(NSError *)error forFrame:(WebFrame *)frame {
    if (frame == [sender mainFrame]) {
        self.done = YES;
    }
}
@end

static BOOL renderPdfPageToPng(PDFDocument *doc, NSUInteger pageIdx, NSString *pngPath) {
    if (!doc || [doc pageCount] == 0) return NO;
    if (pageIdx >= [doc pageCount]) pageIdx = 0;
    PDFPage *page = [doc pageAtIndex:pageIdx];
    NSRect bounds = [page boundsForBox:kPDFDisplayBoxMediaBox];
    if (bounds.size.width <= 0 || bounds.size.height <= 0) {
        bounds = NSMakeRect(0, 0, 720, 540);
    }
    CGFloat targetW = 800.0;
    CGFloat scale = targetW / bounds.size.width;
    CGFloat targetH = round(bounds.size.height * scale);

    NSBitmapImageRep *rep = [[NSBitmapImageRep alloc]
        initWithBitmapDataPlanes:NULL
                      pixelsWide:(NSInteger)targetW
                      pixelsHigh:(NSInteger)targetH
                   bitsPerSample:8
                 samplesPerPixel:4
                        hasAlpha:YES
                        isPlanar:NO
                  colorSpaceName:NSCalibratedRGBColorSpace
                     bytesPerRow:0
                    bitsPerPixel:0];
    if (!rep) return NO;

    [NSGraphicsContext saveGraphicsState];
    NSGraphicsContext *ctx = [NSGraphicsContext graphicsContextWithBitmapImageRep:rep];
    [NSGraphicsContext setCurrentContext:ctx];

    [[NSColor whiteColor] setFill];
    NSRectFill(NSMakeRect(0, 0, targetW, targetH));

    CGContextRef cg = [ctx CGContext];
    CGContextSaveGState(cg);
    CGContextScaleCTM(cg, scale, scale);
    [page drawWithBox:kPDFDisplayBoxMediaBox toContext:cg];
    CGContextRestoreGState(cg);

    [NSGraphicsContext restoreGraphicsState];

    NSData *pngData = [rep representationUsingType:NSBitmapImageFileTypePNG properties:@{}];
    if (!pngData) return NO;
    return [pngData writeToFile:pngPath atomically:YES];
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        if (argc >= 2 && strcmp(argv[1], "--pdf-thumb") == 0) {
            if (argc < 5) {
                fprintf(stderr, "Usage: qlhtml2pdf --pdf-thumb <input.pdf> <page_idx_0_based> <out.png>\n");
                return 1;
            }
            NSString *pdfPath = [NSString stringWithUTF8String:argv[2]];
            NSUInteger pageIdx = (NSUInteger)atoi(argv[3]);
            NSString *pngPath = [NSString stringWithUTF8String:argv[4]];
            PDFDocument *doc = [[PDFDocument alloc] initWithURL:[NSURL fileURLWithPath:pdfPath]];
            if (renderPdfPageToPng(doc, pageIdx, pngPath)) {
                return 0;
            }
            fprintf(stderr, "Failed to render thumbnail from %s\n", [pdfPath UTF8String]);
            return 2;
        }

        if (argc < 3) {
            fprintf(stderr, "Usage: qlhtml2pdf <Preview.html> <output.pdf> [thumb.png] [thumb_page_idx]\n");
            return 1;
        }
        NSString *htmlPath = [NSString stringWithUTF8String:argv[1]];
        NSString *outPath = [NSString stringWithUTF8String:argv[2]];
        NSString *thumbPath = (argc >= 4) ? [NSString stringWithUTF8String:argv[3]] : nil;
        NSUInteger thumbPageIdx = (argc >= 5) ? (NSUInteger)atoi(argv[4]) : 0;

        [NSApplication sharedApplication];
        NSRect initRect = NSMakeRect(0, 0, 1060, 800);
        WebView *webView = [[WebView alloc] initWithFrame:initRect frameName:nil groupName:nil];
        [webView setShouldUpdateWhileOffscreen:YES];
        [[webView preferences] setShouldPrintBackgrounds:YES];

        LoaderDelegate *del = [[LoaderDelegate alloc] init];
        [webView setFrameLoadDelegate:del];

        NSURL *url = [NSURL fileURLWithPath:htmlPath];
        [[webView mainFrame] loadRequest:[NSURLRequest requestWithURL:url]];

        NSDate *timeout = [NSDate dateWithTimeIntervalSinceNow:15.0];
        while (!del.done && [timeout timeIntervalSinceNow] > 0) {
            [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode beforeDate:[NSDate dateWithTimeIntervalSinceNow:0.04]];
        }
        NSDate *extra = [NSDate dateWithTimeIntervalSinceNow:0.25];
        while ([extra timeIntervalSinceNow] > 0) {
            [[NSRunLoop currentRunLoop] runMode:NSDefaultRunLoopMode beforeDate:[NSDate dateWithTimeIntervalSinceNow:0.04]];
        }

        NSString *normJS =
            @"document.body.style.background = '#ffffff';"
             "document.body.style.margin = '0';"
             "document.body.style.padding = '0';"
             "if (document.querySelectorAll('div.slide, div.slideStyle').length === 0) {"
             "  var bodyDivs = document.querySelectorAll('body > div');"
             "  for (var b = 0; b < bodyDivs.length; b++) {"
             "    if (bodyDivs[b].querySelector('img[src$=\".pdf\"]')) {"
             "      bodyDivs[b].classList.add('slideStyle');"
             "    }"
             "  }"
             "}"
             "var keySlides = document.querySelectorAll('div.slideStyle');"
             "if (keySlides.length > 0) {"
             "  var notes = document.querySelectorAll('.notesStyle');"
             "  for (var n = 0; n < notes.length; n++) { notes[n].style.display = 'none'; }"
             "  for (var k = 0; k < keySlides.length; k++) {"
             "    keySlides[k].style.margin = '0';"
             "    keySlides[k].style.boxShadow = 'none';"
             "    keySlides[k].style.webkitBoxShadow = 'none';"
             "  }"
             "}"
             "var slides = document.querySelectorAll('div.slide');"
             "if (slides.length > 0) {"
             "  var styleEl = document.createElement('style');"
             "  styleEl.textContent = '"
             "    img:not([src]) { display: none !important; } "
             "    img[src$=\".pdf\"] { mix-blend-mode: multiply; } "
             "    p, div, span, td { word-wrap: normal !important; overflow-wrap: normal !important; } "
             "  ';"
             "  document.head.appendChild(styleEl);"
             "}"
             "for (var s = 0; s < slides.length; s++) {"
             "  var slide = slides[s];"
             "  slide.style.margin = '0';"
             "  slide.style.boxShadow = 'none';"
             "  slide.style.webkitBoxShadow = 'none';"
             "  var children = slide.children;"
             "  for (var c = 0; c < children.length; c++) {"
             "    var box = children[c];"
             "    if (box.tagName !== 'DIV' || box.classList.contains('s0')) continue;"
             "    var st = box.getAttribute('style') || '';"
             "    var txt = (box.innerText || '').replace(/\\u00a0/g, '').trim();"
             "    var hasImg = box.querySelector('img[src]') !== null;"
             "    var hasBorderOrBg = (st.indexOf('border') !== -1 || st.indexOf('background-color') !== -1);"
             "    if (!txt && !hasImg && st.indexOf('background-color:#ffffff') !== -1 && st.indexOf('border') !== -1) {"
             "      box.style.border = 'none';"
             "      continue;"
             "    }"
             "    if (!txt) continue;"
             "    var origW = parseFloat(box.style.width) || box.clientWidth;"
             "    var origH = parseFloat(box.style.height) || box.clientHeight;"
             "    var origL = parseFloat(box.style.left) || 0;"
             "    if (hasBorderOrBg && box.scrollHeight <= origH + 4 && box.scrollWidth <= origW + 4) continue;"
             "    var innerDivs = box.querySelectorAll('div');"
             "    for (var d = 0; d < innerDivs.length; d++) {"
             "      innerDivs[d].style.marginLeft = '0px';"
             "      innerDivs[d].style.marginRight = '0px';"
             "      innerDivs[d].style.marginTop = '0px';"
             "      innerDivs[d].style.marginBottom = '0px';"
             "      if (!hasBorderOrBg && getComputedStyle(innerDivs[d]).display === 'table') {"
             "        innerDivs[d].style.width = '100%';"
             "        innerDivs[d].style.height = 'auto';"
             "      }"
             "    }"
             "    box.style.overflow = 'visible';"
             "    /* Check for 90-deg rotated vertical text box */"
             "    if (origW <= 85 && origH >= origW * 2.0 && txt.length >= 5 && box.scrollWidth > origW + 4) {"
             "      var rotWrap = document.createElement('div');"
             "      rotWrap.style.width = origH + 'px';"
             "      rotWrap.style.transform = 'rotate(-90deg)';"
             "      rotWrap.style.transformOrigin = 'center center';"
             "      rotWrap.style.textAlign = 'center';"
             "      while (box.firstChild) { rotWrap.appendChild(box.firstChild); }"
             "      box.style.display = 'flex';"
             "      box.style.alignItems = 'center';"
             "      box.style.justifyContent = 'center';"
             "      box.appendChild(rotWrap);"
             "      continue;"
             "    }"
             "    /* Determine max font size and paragraph count in box */"
             "    var paras = box.querySelectorAll('p');"
             "    var textEls = box.querySelectorAll('p, span');"
             "    var maxFs = 18;"
             "    for (var t = 0; t < textEls.length; t++) {"
             "      var fs = parseFloat(getComputedStyle(textEls[t]).fontSize) || 0;"
             "      if (fs > maxFs) maxFs = fs;"
             "    }"
             "    var numLinesExpected = 0;"
             "    var maxParaLen = 0;"
             "    for (var p = 0; p < paras.length; p++) {"
             "      var brs = paras[p].querySelectorAll('br').length;"
             "      numLinesExpected += (1 + brs);"
             "      var plen = (paras[p].innerText || '').trim().length;"
             "      if (plen > maxParaLen) maxParaLen = plen;"
             "    }"
             "    if (numLinesExpected < 1) numLinesExpected = 1;"
             "    var isSingleWord = !/\\s/.test(txt);"
             "    var isTitleBox = (!hasBorderOrBg && paras.length === 1 && numLinesExpected === 1 && maxFs >= 24 && txt.length <= 55);"
             "    var isShortPointText = (!hasBorderOrBg && maxParaLen <= 44 && origH <= maxFs * 2.1 * numLinesExpected);"
             "    if (isSingleWord || isTitleBox || isShortPointText) {"
             "      for (var p = 0; p < paras.length; p++) {"
             "        if (paras[p].querySelectorAll('br').length === 0) {"
             "          paras[p].style.whiteSpace = 'nowrap';"
             "        }"
             "      }"
             "      var maxNowrapW = isTitleBox ? 745 : Math.min(714 - origL, origW * 1.25 + 24);"
             "      if (!isSingleWord && !isTitleBox && box.scrollWidth > maxNowrapW) {"
             "        for (var p = 0; p < paras.length; p++) {"
             "          paras[p].style.whiteSpace = 'normal';"
             "        }"
             "      }"
             "    }"
             "    if (!hasBorderOrBg) {"
             "      var pFirst = paras.length > 0 ? paras[0] : null;"
             "      var align = pFirst ? getComputedStyle(pFirst).textAlign : 'left';"
             "      var neededW = box.scrollWidth + 6;"
             "      if (align === 'center') {"
             "        var centerX = origL + origW / 2.0;"
             "        var maxAllowedW = Math.min(712, Math.min(centerX, 720 - centerX) * 2.0 - 6);"
             "        var targetW = Math.min(neededW, Math.min(origW * 1.25 + 24, maxAllowedW));"
             "        var newW = Math.min(maxAllowedW, Math.max(origW, targetW));"
             "        box.style.width = newW + 'px';"
             "        box.style.left = (centerX - newW / 2.0) + 'px';"
             "      } else {"
             "        var maxAllowedW = Math.min(714 - origL, origW * 1.18 + 18);"
             "        var newW = Math.min(maxAllowedW, Math.max(origW, neededW));"
             "        box.style.width = newW + 'px';"
             "      }"
             "    }"
             "    /* If box still overflows its original PowerPoint height or width, scale font down */"
             "    for (var step = 0; step < 10; step++) {"
             "      if (box.scrollHeight <= origH + 6 && box.scrollWidth <= box.clientWidth + 2) break;"
             "      for (var t = 0; t < textEls.length; t++) {"
             "        var el = textEls[t];"
             "        var fs = parseFloat(getComputedStyle(el).fontSize);"
             "        if (fs > 8) el.style.fontSize = (fs * 0.94) + 'px';"
             "        var pt = parseFloat(getComputedStyle(el).paddingTop);"
             "        if (pt > 1) el.style.paddingTop = (pt * 0.85) + 'px';"
             "      }"
             "    }"
             "  }"
             "}";

        [webView stringByEvaluatingJavaScriptFromString:normJS];

        NSString *countStr = [webView stringByEvaluatingJavaScriptFromString:@"document.querySelectorAll('div.slide, div.slideStyle').length.toString()"];
        int slideCount = [countStr intValue];
        if (slideCount <= 0) {
            fprintf(stderr, "No slide elements found in %s\n", [htmlPath UTF8String]);
            return 2;
        }

        NSView *docView = [[[webView mainFrame] frameView] documentView];
        [docView layout];
        NSRect fullBounds = [docView bounds];
        [webView setFrame:fullBounds];
        [docView setFrame:fullBounds];

        NSString *rectsStr = [webView stringByEvaluatingJavaScriptFromString:
            @"var slides = document.querySelectorAll('div.slide, div.slideStyle');"
             "var rects = [];"
             "for (var i = 0; i < slides.length; i++) {"
             "  var s = slides[i];"
             "  if (!s.classList.contains('slideStyle')) {"
             "    var txt = (s.innerText || '').replace(/\\u00a0/g, '').trim();"
             "    var imgs = s.querySelectorAll('img[src]').length;"
             "    var shapes = s.querySelectorAll('div').length;"
             "    if (!txt && imgs === 0 && shapes <= 5) continue;"
             "  }"
             "  var r = s.getBoundingClientRect();"
             "  rects.push(r.left + ',' + r.top + ',' + r.width + ',' + r.height);"
             "}"
             "rects.join(';');"
        ];

        NSArray *rectItems = [rectsStr componentsSeparatedByString:@";"];
        PDFDocument *outDoc = [[PDFDocument alloc] init];

        for (NSString *item in rectItems) {
            NSArray *parts = [item componentsSeparatedByString:@","];
            if ([parts count] != 4) continue;
            CGFloat x = [parts[0] doubleValue];
            CGFloat y = [parts[1] doubleValue];
            CGFloat w = [parts[2] doubleValue];
            CGFloat h = [parts[3] doubleValue];
            if (w <= 0 || h <= 0) continue;

            NSRect slideRect;
            if ([docView isFlipped]) {
                slideRect = NSMakeRect(x, y, w, h);
            } else {
                slideRect = NSMakeRect(x, fullBounds.size.height - y - h, w, h);
            }

            NSData *pdfData = [docView dataWithPDFInsideRect:slideRect];
            if (pdfData) {
                PDFDocument *pageDoc = [[PDFDocument alloc] initWithData:pdfData];
                if (pageDoc && [pageDoc pageCount] > 0) {
                    PDFPage *page = [pageDoc pageAtIndex:0];
                    [outDoc insertPage:page atIndex:[outDoc pageCount]];
                }
            }
        }

        if ([outDoc pageCount] > 0) {
            [outDoc writeToFile:outPath];
            if (thumbPath) {
                renderPdfPageToPng(outDoc, thumbPageIdx, thumbPath);
            }
            printf("Wrote %lu slides to %s\n", (unsigned long)[outDoc pageCount], [outPath UTF8String]);
            return 0;
        } else {
            fprintf(stderr, "Failed to generate PDF pages\n");
            return 3;
        }
    }
}
