(function () {
  "use strict";

  const components = {};

  function mount(root) {
    const islands = root.querySelectorAll("[data-django-mui-island]");
    islands.forEach((island) => {
      const payloadId = island.dataset.djangoMuiPayloadId;
      if (!payloadId) {
        console.warn("django_mui: island payload id missing");
        return;
      }
      const payloadNode = document.getElementById(payloadId);
      if (!payloadNode || payloadNode.tagName !== "SCRIPT") {
        console.warn("django_mui: island payload node missing", payloadId);
        return;
      }

      let payload;
      try {
        payload = JSON.parse(payloadNode.textContent || "{}");
      } catch (error) {
        console.warn("django_mui: invalid island payload JSON", error);
        return;
      }
      if (!payload || payload.version === undefined || !payload.component) {
        console.warn("django_mui: island payload missing required fields");
        return;
      }
      if (payload.version !== 1) {
        console.warn("django_mui: unsupported island payload version", payload.version);
        return;
      }

      const component = components[payload.component];
      if (!component) {
        console.warn("django_mui: unregistered island component", payload.component);
        return;
      }

      component(island, payload.props || {});
    });
  }

  window.DjangoMuiIslands = {
    register: function (name, component) {
      components[name] = component;
    },
    mount: function () {
      mount(document);
    },
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", window.DjangoMuiIslands.mount);
  } else {
    window.DjangoMuiIslands.mount();
  }
})();
