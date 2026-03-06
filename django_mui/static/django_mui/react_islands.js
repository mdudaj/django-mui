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

  function getCsrfTokenFromCookie(cookieName) {
    const name = cookieName || "csrftoken";
    const match = document.cookie.match(new RegExp("(?:^|;\\s*)" + name + "=([^;]+)"));
    return match ? decodeURIComponent(match[1]) : "";
  }

  window.DjangoMuiIslands.register("WorkflowStatusCard", function (island, props) {
    const endpoint = props.endpoint || "";
    if (!endpoint) {
      return;
    }

    const card = document.createElement("section");
    const state = document.createElement("p");
    const actions = document.createElement("div");
    const messages = document.createElement("ul");
    let currentState = props.state || "";
    let currentTransitions = Array.isArray(props.allowed_transitions) ? props.allowed_transitions : [];

    function render() {
      state.textContent = "State: " + currentState;
      actions.textContent = "";
      messages.textContent = "";

      currentTransitions.forEach(function (transition) {
        const button = document.createElement("button");
        button.type = "button";
        button.textContent = transition;
        button.addEventListener("click", function () {
          messages.textContent = "";
          const token =
            props.csrfmiddlewaretoken ||
            getCsrfTokenFromCookie(props.csrf_cookie_name);
          const body = new URLSearchParams({
            transition: transition,
            object_id: String(props.object_id || ""),
            csrfmiddlewaretoken: token,
          });
          fetch(endpoint, {
            method: "POST",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
              "X-CSRFToken": token,
            },
            credentials: "same-origin",
            body: body.toString(),
          })
            .then(function (response) {
              return response.json().then(function (payload) {
                const serverMessages = Array.isArray(payload.messages)
                  ? payload.messages
                  : [];
                return {
                  state: payload.state,
                  allowed_transitions: payload.allowed_transitions,
                  messages:
                    !response.ok && !serverMessages.length
                      ? ["Transition rejected."]
                      : serverMessages,
                };
              });
            })
            .then(function (payload) {
              currentState = payload.state || currentState;
              currentTransitions = Array.isArray(payload.allowed_transitions)
                ? payload.allowed_transitions
                : [];
              (payload.messages || []).forEach(function (message) {
                const item = document.createElement("li");
                item.textContent = String(message);
                messages.appendChild(item);
              });
              render();
            })
            .catch(function (error) {
              console.warn("django_mui: transition request failed", error);
              const item = document.createElement("li");
              item.textContent = "Transition request failed.";
              messages.appendChild(item);
            });
        });
        actions.appendChild(button);
      });
    }

    card.appendChild(state);
    card.appendChild(actions);
    card.appendChild(messages);
    island.appendChild(card);
    render();
  });

  window.DjangoMuiIslands.register("FormFieldWidgetHint", function (island, props) {
    const hint = document.createElement("small");
    hint.className = "mui-field__help-text";
    hint.textContent = props.message || "Field widget island mounted.";
    island.appendChild(hint);
  });

  window.DjangoMuiIslands.register("TodoDashboardStatsCard", function (island, props) {
    const fallback = island.parentElement
      ? island.parentElement.querySelector("[data-django-mui-stats-fallback]")
      : null;
    const chips = [
      {
        label: "Total: " + String(props.total_count || 0),
        variant: "neutral",
      },
      {
        label: "Open: " + String(props.open_count || 0),
        variant: "warning",
      },
      {
        label: "Done: " + String(props.completed_count || 0),
        variant: "success",
      },
    ];
    const card = document.createElement("section");
    card.className = "mui-card";
    const title = document.createElement("h3");
    title.className = "mui-card__title";
    title.textContent = props.title || "Todo overview";
    const chipList = document.createElement("ul");
    chipList.className = "mui-chip-set";
    chips.forEach(function (chip) {
      const item = document.createElement("li");
      const chipElement = document.createElement("span");
      chipElement.className = "mui-status-chip mui-status-chip--" + chip.variant;
      chipElement.textContent = chip.label;
      item.appendChild(chipElement);
      chipList.appendChild(item);
    });
    card.appendChild(title);
    card.appendChild(chipList);
    island.appendChild(card);
    if (fallback) {
      fallback.hidden = true;
    }
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", window.DjangoMuiIslands.mount);
  } else {
    window.DjangoMuiIslands.mount();
  }
})();
