<template>
  <div class="main-header">
    <div class="logo">
      <img src="@/assets/evi_logo_sq.png" alt />
    </div>

    <div @click="sideBarToggle" class="menu-toggle">
      <div></div>
      <div></div>
      <div></div>
    </div>

    <div style="margin: auto"></div>

    <div class="header-part-right">
      <!-- Full screen toggle -->
      <i
        class="i-Full-Screen header-icon d-none d-sm-inline-block"
        @click="handleFullScreen"
      ></i>
      <!-- <i class="i-Full-Screen header-icon d-none d-sm-inline-block" data-fullscreen></i> -->

      <!-- User avatar dropdown -->
      <div class="dropdown">
        <b-dropdown
          id="dropdown-1"
          text="Dropdown Button"
          class="m-md-2 user col align-self-end"
          toggle-class="text-decoration-none"
          no-caret
          variant="link"
        >
          <template slot="button-content">
            <img
              src="https://image.flaticon.com/icons/svg/599/599305.svg"
              id="userDropdown"
              alt
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            />
          </template>

          <div class="dropdown-menu-right" aria-labelledby="userDropdown">
            <div class="dropdown-header">
              {{ username }}
            </div>
            <!-- <a class="dropdown-item" href="/app/sessions/signIn/" @click.prevent="logoutUser">Log out</a> -->
            <a class="dropdown-item" to="signIn" @click.prevent="logoutUser">Log out</a>
          </div>
        </b-dropdown>
      </div>
    </div>
  </div>

  <!-- header top menu end -->
</template>
<script>
import Util from "@/utils";
import Sidebar from "./Sidebar";
import searchComponent from "../common/search";
import { isMobile } from "mobile-device-detect";
import { mapGetters, mapActions } from "vuex";
import { mixin as clickaway } from "vue-clickaway";
import { apiService } from "@/common/api.service.js";

export default {
  mixins: [clickaway],
  components: {
    Sidebar,
    searchComponent
  },

  data() {
    return {
      isDisplay: true,
      username: null,
      isStyle: true,
      isSearchOpen: false,
      isMouseOnMegaMenu: true,
      isMegaMenuOpen: false
    };
  },
  mounted() {
    let name = JSON.parse(localStorage.userInfo)
    this.username = name.toUpperCase()
  },
  computed: {
    ...mapGetters(["getSideBarToggleProperties"])
  },

  methods: {
    ...mapActions([
      "changeSecondarySidebarProperties",

      "changeSidebarProperties",
      "changeThemeMode",
      "signOut"
    ]),

    // megaMenuToggle() {
    //   this.isMegaMenuOpen = false;

    //   console.log("work");
    // },

    handleFullScreen() {
      Util.toggleFullScreen();
    },
    logoutUser() {
      let endpoint = `/api/rest-auth/logout/`
      apiService(endpoint, "POST")

      this.logoutUserApp()
    },

    logoutUserApp() {
      setTimeout(() => {
        this.$router.push("/app/sessions/signIn");
        this.signOut();
      }, 1000);
    },

    closeMegaMenu() {
      this.isMegaMenuOpen = false;
      // console.log(this.isMouseOnMegaMenu);
      // if (!this.isMouseOnMegaMenu) {
      //   this.isMegaMenuOpen = !this.isMegaMenuOpen;
      // }
    },
    toggleMegaMenu() {
      this.isMegaMenuOpen = !this.isMegaMenuOpen;
    },

    sideBarToggle(el) {
      if (
        this.getSideBarToggleProperties.isSideNavOpen &&
        this.getSideBarToggleProperties.isSecondarySideNavOpen &&
        isMobile
      ) {
        this.changeSidebarProperties();
        this.changeSecondarySidebarProperties();
      } else if (
        this.getSideBarToggleProperties.isSideNavOpen &&
        this.getSideBarToggleProperties.isSecondarySideNavOpen
      ) {
        this.changeSecondarySidebarProperties();
      } else if (this.getSideBarToggleProperties.isSideNavOpen) {
        this.changeSidebarProperties();
      } else if (
        !this.getSideBarToggleProperties.isSideNavOpen &&
        !this.getSideBarToggleProperties.isSecondarySideNavOpen &&
        !this.getSideBarToggleProperties.isActiveSecondarySideNav
      ) {
        this.changeSidebarProperties();
      } else if (
        !this.getSideBarToggleProperties.isSideNavOpen &&
        !this.getSideBarToggleProperties.isSecondarySideNavOpen
      ) {
        // console.log("4");

        this.changeSidebarProperties();
        this.changeSecondarySidebarProperties();
        // console.log("4");
      }
    }
  }
};
</script>



