(function () {
  "use strict";

  const components = {};

  function mount(root) {
    const islands = root.querySelectorAll("[data-django-mui-island]");
    islands.forEach((island) => {
      const payloadNode = island.nextElementSibling;
      if (!payloadNode || payloadNode.dataset.djangoMuiIslandPayload === undefined) {
        return;
      }

      let payload;
      try {
        payload = JSON.parse(payloadNode.textContent || "{}");
      } catch (error) {
        return;
      }
      if (!payload || payload.version === undefined || !payload.component) {
        return;
      }

      const component = components[payload.component];
      if (!component) {
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
