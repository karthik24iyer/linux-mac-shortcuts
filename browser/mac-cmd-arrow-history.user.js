// ==UserScript==
// @name        Mac Cmd+Left/Right history
// @description Cmd+Left/Right (sent as Home/End by Toshy) go back/forward when not typing
// @match       *://*/*
// @run-at      document-start
// @grant       none
// ==/UserScript==

function isEditable(el) {
  while (el?.shadowRoot?.activeElement) el = el.shadowRoot.activeElement;
  return !!el && (el.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName));
}

addEventListener('keydown', e => {
  if (e.ctrlKey || e.altKey || e.metaKey || e.shiftKey || isEditable(document.activeElement)) return;
  if (e.key === 'Home') { e.preventDefault(); history.back(); }
  else if (e.key === 'End') { e.preventDefault(); history.forward(); }
}, true);
