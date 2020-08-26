<template>
  <div>
    <router-view></router-view>

    <customizer></customizer>
  </div>
</template>


<script>
import { mapGetters } from "vuex";
import { apiService } from "@/common/api.service.js";

export default {
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["getThemeMode"]),
    themeName() {
      return this.getThemeMode.dark ? "dark-theme" : " ";
    },
    rtl() {
      return this.getThemeMode.rtl ? "rtl" : " ";
    }
  },
  methods: {
    async setUserInfo() {
      // add the username of the logged in user to localStorage
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
    }
  },
  metaInfo() {
    return {
      // if no subcomponents specify a metaInfo.title, this title will be used
      title: "EVI",
      // all titles will be injected into this template
      titleTemplate: "%s | EVI",
      bodyAttrs: {
        class: [this.themeName, "text-left"]
      },
      htmlAttrs: {
        dir: this.rtl
      }
    };
    
  }
};
</script>

<style>

</style>


