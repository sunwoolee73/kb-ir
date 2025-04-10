
function resizeIframe(iframe) {
  setTimeout(function () {
    try {
      iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
    } catch (e) {
      console.warn('iframe 자동 높이 조절 실패:', e);
    }
  }, 500);
}
