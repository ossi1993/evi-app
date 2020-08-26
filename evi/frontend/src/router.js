import Vue from "vue";
import store from "./store";
// import {isMobile} from "mobile-device-detect";
import Router from "vue-router";
import NProgress from "nprogress";
import authenticate from "./auth/authenticate";

Vue.use(Router);

// create new router

const routes = [
  //webpackChunkName app
  {
    path: "/",
    component: () => import("./views/app"), 
    beforeEnter: authenticate,
    redirect: "/app/dashboard",

    children: [
      // Dashboard
      {
        path: "/app/dashboard",
        component: () => import("./views/app/dashboards/dashboard"),
      },
      // Manufacturer
      {
        path: "/app/manufacturer",
        component: () => import("./views/app/manufacturer/list")
      },
      // Supplier
      {
        path: "/app/supplier",
        component: () => import("./views/app/supplier/list")
      },
      // Order
      {
        path: "/app/order",
        component: () => import("./views/app/order/list")
      },
      // Device
      {
        path: "/app/device",
        component: () => import("./views/app/device"),
        redirect: "/app/device/device-list",
        children: [
          {
            path: "device-list",
            component: () => import("./views/app/device/device-list")
          },
          {
            path: "model-list",
            component: () => import("./views/app/device/model-list")
          },
          {
            path: "device-attributes",
            component: () => import("./views/app/device/device-attributes")
          },
          {
            path: "device-templates",
            component: () => import("./views/app/device/device-templates")
          },
        ]
      },
      // Item
      {
        path: "/app/item",
        component: () => import("./views/app/item"),
        redirect: "/app/item/list",
        children: [
          {
            path: "item-list",
            component: () => import("./views/app/item/item-list")
          },
          {
            path: "item-attributes",
            component: () => import("./views/app/item/item-attributes")
          },
          {
            path: "item-import",
            component: () => import("./views/app/item/item-import")
          },
          {
            path: "item-templates",
            component: () => import("./views/app/item/item-templates")
          },
        ]
      },
      // Inspection
      {
        path: "/app/inspection",
        component: () => import("./views/app/inspection"),
        redirect: "/app/inspection/list-inspection",
        children: [
          {
            path: "inspection-list",
            component: () => import("./views/app/inspection/inspection-list")
          },
          {
            path: "sample",
            component: () => import("./views/app/inspection/sample")
          },
          {
            path: "sample-attributes",
            component: () => import("./views/app/inspection/sample-attributes")
          },
          {
            path: "templates",
            component: () => import("./views/app/inspection/templates")
          },
          {
            path: "inspection",
            component: () => import("./views/app/inspection/inspection")
          },
          {
            path: "inspection-attributes",
            component: () => import("./views/app/inspection/inspection-attributes")
          },
        ]
      },
    ]
  },
  // sessions
  {
    path: "/app/sessions",
    component: () => import("./views/app/sessions"),
    redirect: "/app/sessions/signIn",
    children: [
      {
        path: "signIn",
        component: () => import("./views/app/sessions/signIn")
      },
      {
        path: "signUp",
        component: () => import("./views/app/sessions/signUp")
      },
      {
        path: "forgot",
        component: () => import("./views/app/sessions/forgot")
      }
    ]
  },

  {
    path: "/vertical-sidebar",
    component: () => import("./containers/layouts/verticalSidebar")
  },
  {
    path: "*",
    component: () => import("./views/app/pages/notFound")
  }
];

const router = new Router({
  mode: "history",
  linkActiveClass: "open",
  routes,
  scrollBehavior(to, from, savedPosition) {
    return {x: 0, y: 0};
  }
});

router.beforeEach((to, from, next) => {
  // If this isn't an initial page load.
  if (to.path) {
    // Start the route progress bar.

    NProgress.start();
    NProgress.set(0.1);
  }
  next();
});

router.afterEach(() => {
  // Remove initial loading
  const gullPreLoading = document.getElementById("loading_wrap");
  if (gullPreLoading) {
    gullPreLoading.style.display = "none";
  }
  // Complete the animation of the route progress bar.
  setTimeout(() => NProgress.done(), 500);
  // NProgress.done();
  // if (isMobile) {
  if (window.innerWidth <= 1200) {
    // console.log("mobile");
    store.dispatch("changeSidebarProperties");
    if (store.getters.getSideBarToggleProperties.isSecondarySideNavOpen) {
      store.dispatch("changeSecondarySidebarProperties");
    }

    if (store.getters.getCompactSideBarToggleProperties.isSideNavOpen) {
      store.dispatch("changeCompactSidebarProperties");
    }
  } else {
    if (store.getters.getSideBarToggleProperties.isSecondarySideNavOpen) {
      store.dispatch("changeSecondarySidebarProperties");
    }

    // store.state.sidebarToggleProperties.isSecondarySideNavOpen = false;
  }
});

export default router;
