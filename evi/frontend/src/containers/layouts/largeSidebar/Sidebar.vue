<template>
  <div
    class="side-content-wrap"
    @mouseenter="isMenuOver = true"
    @mouseleave="isMenuOver = false"
    @touchstart="isMenuOver = true"
  >
    <vue-perfect-scrollbar
      :settings="{ suppressScrollX: true, wheelPropagation: false }"
      :class="{ open: getSideBarToggleProperties.isSideNavOpen }"
      ref="myData"
      class="sidebar-left rtl-ps-none ps scroll"
    >
      <div>
        <ul class="navigation-left">
          <!-- DASHBOARD SECTION -->
          <li @mouseenter="toggleTriangle" @mouseleave="toggleSelectedParentMenu" :class="{ active: selectedParentMenu == 'dashboard' }" class="nav-item" data-item="dashboard">
            <router-link tag="a" class="nav-item-hold" to="/app/dashboard">
              <i class="nav-icon i-Bar-Chart"></i>
              <span class="nav-text">{{ $t('dashboard') }}</span>
            </router-link>
            <div class="triangle"></div>
          </li>
          <!-- INSPECTION SECTION -->
          <li @mouseenter="toggleSubMenu" class="nav-item" :class="{ active: selectedParentMenu == 'inspection' }" data-item="inspection">
            <a class="nav-item-hold" href="#">
              <i class="nav-icon i-File-Clipboard-File--Text"></i>
              <span class="nav-text">Inspection</span>
            </a>
            <div class="triangle"></div>
          </li>
          <!-- ITEM SECTION -->
          <li @mouseenter="toggleSubMenu" class="nav-item" :class="{ active: selectedParentMenu == 'item' }" data-item="item">
            <a class="nav-item-hold" href="#">
              <i class="nav-icon i-Eci-Icon"></i>
              <span class="nav-text">Item</span>
            </a>
            <div class="triangle"></div>
          </li>
          <!-- DEVICE SECTION -->
          <li @mouseenter="toggleSubMenu" class="nav-item" :class="{ active: selectedParentMenu == 'device' }" data-item="device">
            <a class="nav-item-hold" href="#">
              <i class="nav-icon i-Smartphone--Secure"></i>
              <span class="nav-text">Device</span>
            </a>
            <div class="triangle"></div>
          </li>
          <!-- ORDER SECTION -->
          <li @mouseenter="toggleTriangle" @mouseleave="toggleSelectedParentMenu" class="nav-item" :class="{ active: selectedParentMenu == 'order' }" data-item="order">
            <router-link tag="a" class="nav-item-hold" to="/app/order">
              <i class="nav-icon i-Full-Basket"></i>
              <span class="nav-text">Order</span>
            </router-link>
            <div class="triangle"></div>
          </li>
          <!-- SUPPLIER SECTION -->
          <li @mouseenter="toggleTriangle" @mouseleave="toggleSelectedParentMenu" class="nav-item" :class="{ active: selectedParentMenu == 'supplier' }" data-item="supplier">
            <router-link tag="a" class="nav-item-hold" to="/app/supplier">
              <i class="nav-icon i-Box-Full"></i>
              <span class="nav-text">Supplier</span>
            </router-link>
            <div class="triangle"></div>
          </li>
          <!-- MANUFACTURER SECTION -->
          <li @mouseenter="toggleTriangle" @mouseleave="toggleSelectedParentMenu" class="nav-item" :class="{ active: selectedParentMenu == 'manufacturer' }" data-item="manufacturer">
            <router-link tag="a" class="nav-item-hold" to="/app/manufacturer">
              <i class="nav-icon i-Factory"></i>
              <span class="nav-text">Manufacturer</span>
            </router-link>
            <div class="triangle"></div>
          </li>
        </ul>
      </div>
    </vue-perfect-scrollbar>

    <vue-perfect-scrollbar
      :class="{ open: getSideBarToggleProperties.isSecondarySideNavOpen }"
      :settings="{ suppressScrollX: true, wheelPropagation: false }"
      class="sidebar-left-secondary ps rtl-ps-none">

      <div ref="sidebarChild">

        <ul class="childNav d-none" data-parent="ui-kits" :class="{ 'd-block': selectedParentMenu == 'inspection' }">
          <li class="nav-item">
            <router-link tag="a" class to="/app/inspection/inspection-list">
              <i class="nav-icon i-Belt-3"></i>
              <span class="item-name">List Inspections</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/inspection/templates">
              <i class="nav-icon i-File"></i>
              <span class="item-name">Templates</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/inspection/inspection-attributes">
              <i class="nav-icon i-Atom"></i>
              <span class="item-name">Inspection Attributes</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/inspection/sample">
              <i class="nav-icon i-Add"></i>
              <span class="item-name">Sample</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/inspection/sample-attributes">
              <i class="nav-icon i-Atom"></i>
              <span class="item-name">Sample Attributes</span>
            </router-link>
          </li>
        </ul>

        <ul class="childNav d-none" data-parent="extrakits" :class="{ 'd-block': selectedParentMenu == 'item' }">
          <li class="nav-item">
            <router-link tag="a" class to="/app/item/item-list">
              <i class="nav-icon i-Belt-3"></i>
              <span class="item-name">List Items</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/item/item-attributes">
              <i class="nav-icon i-Atom"></i>
              <span class="item-name">Item Attributes</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/item/item-import">
              <i class="nav-icon i-Upload"></i>
              <span class="item-name">Item Import</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/item/item-templates">
              <i class="nav-icon i-File"></i>
              <span class="item-name">Templates</span>
            </router-link>
          </li>
        </ul>

        <ul class="childNav d-none" data-parent="apps" :class="{ 'd-block': selectedParentMenu == 'device' }">
          <li class="nav-item">
            <router-link tag="a" class to="/app/device/device-list">
              <i class="nav-icon i-Belt-3"></i>
              <span class="item-name">List Devices</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/device/model-list">
              <i class="nav-icon i-Belt-3"></i>
              <span class="item-name">List Models</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/device/device-attributes">
              <i class="nav-icon i-Atom"></i>
              <span class="item-name">Device Attributes</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/device/device-templates">
              <i class="nav-icon i-File"></i>
              <span class="item-name">Templates</span>
            </router-link>
          </li>
        </ul>

        <ul class="childNav d-none" data-parent="apps" :class="{ 'd-block': selectedParentMenu == 'order' }">
          <li class="nav-item">
            <router-link tag="a" class to="/app/inspection/list-orders">
              <i class="nav-icon i-Basket"></i>
              <span class="item-name">List Orders</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/inspection/list-order-items">
              <i class="nav-icon i-Add"></i>
              <span class="item-name">List Order Items</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class to="/app/inspection/list-order-models">
              <i class="nav-icon i-Atom"></i>
              <span class="item-name">List Order Models</span>
            </router-link>
          </li>
        </ul>

      </div>
    </vue-perfect-scrollbar>
    <div
      @click="removeOverlay()"
      class="sidebar-overlay"
      :class="{ open: getSideBarToggleProperties.isSecondarySideNavOpen }"
    ></div>
  </div>
  <!--=============== Left side End ================-->
</template>

<script>
import Topnav from "./TopNav";
import { isMobile } from "mobile-device-detect";

import { mapGetters, mapActions } from "vuex";

export default {
  components: {
    Topnav
  },

  data() {
    return {
      isDisplay: true,
      isMenuOver: false,
      isStyle: true,
      selectedParentMenu: "",
      isMobile,
      show: false,
    };
  },
  mounted() {
    this.toggleSelectedParentMenu();
    window.addEventListener("resize", this.handleWindowResize);
    document.addEventListener("click", this.returnSelectedParentMenu);
    this.handleWindowResize();
  },

  beforeDestroy() {
    document.removeEventListener("click", this.returnSelectedParentMenu);
    window.removeEventListener("resize", this.handleWindowResize);
  },
  computed: {
    ...mapGetters(["getSideBarToggleProperties"])
  },

  methods: {
    ...mapActions([
      "changeSecondarySidebarProperties",
      "changeSecondarySidebarPropertiesViaMenuItem",
      "changeSecondarySidebarPropertiesViaOverlay",
      "changeSidebarProperties"
    ]),

    handleWindowResize() {
      //  console.log('not working is Mobile');
      if (window.innerWidth <= 1200) {
        if (this.getSideBarToggleProperties.isSideNavOpen) {
          this.changeSidebarProperties();
        }
        if (this.getSideBarToggleProperties.isSecondarySideNavOpen) {
          this.changeSecondarySidebarProperties();
        }
      } else {
        if (!this.getSideBarToggleProperties.isSideNavOpen) {
          this.changeSidebarProperties();
        }
      }
    },
    toggleSelectedParentMenu() {
      const currentParentUrl = this.$route.path
        .split("/")
        .filter(x => x !== "")[1];

      if (currentParentUrl !== undefined || currentParentUrl !== null) {
        this.selectedParentMenu = currentParentUrl.toLowerCase();
      } else {
        this.selectedParentMenu = "dashboards";
      }
    },
    toggleSubMenu(e) {
      let childrens = this.$refs.sidebarChild.children;
      let parent = e.target.dataset.item;
      this.selectedParentMenu = parent;
      this.changeSecondarySidebarPropertiesViaMenuItem(true);
    },
    toggleTriangle(e) {
      let parent = e.target.dataset.item;
      this.selectedParentMenu = parent;
      this.changeSecondarySidebarPropertiesViaMenuItem(false);
    },
    toggleTriangleReset(e) {
      this.toggleSelectedParentMenu();
    },
    removeOverlay() {
      this.changeSecondarySidebarPropertiesViaOverlay();
      if (window.innerWidth <= 1200) {
        this.changeSidebarProperties();
      }
      this.toggleSelectedParentMenu();
    },
    returnSelectedParentMenu() {
      if (!this.isMenuOver) {
        this.toggleSelectedParentMenu();
      }
    },

    toggleSidebarDropdwon(event) {
      let dropdownMenus = this.$el.querySelectorAll(".dropdown-sidemenu.open");

      event.currentTarget.classList.toggle("open");

      dropdownMenus.forEach(dropdown => {
        dropdown.classList.remove("open");
      });
    }
  }
};
</script>

<style lang="" scoped>
</style>
