<template>
  <div
    class="auth-layout-wrap"
    :style="{ backgroundImage: 'url(' + bgImage + ')' }"
  >
    <div class="auth-content">
      <div class="card o-hidden">
        <div class="col-12">
          <div class="p-4">
            <div class="auth-logo text-center">
              <img :src="logo" />
            </div>
            <h1 class="mb-3 text-center text-20">Sign In</h1>
            <b-form @submit.prevent="formSubmit">
              <b-form-group label="Username" class="text-12">
                <b-form-input class="form-control-rounded" type="text" v-model="username" required></b-form-input>
              </b-form-group>
              <b-form-group label="Password" class="text-12">
                <b-form-input class="form-control-rounded" type="password" v-model="password"></b-form-input>
              </b-form-group>
              <b-button type="submit" tag="button" class="btn-rounded btn-block mt-2" variant="primary mt-2" :disabled="loading">SignIn</b-button>
              <div v-once class="typo__p" v-if="loading">
                <div class="spinner sm spinner-primary mt-3"></div>
              </div>
              <b-button to="signUp" block variant="outline-primary mt-2" class="btn-rounded">Create an account</b-button>
            </b-form>
            <div class="mt-3 text-center">
              <router-link to="forgot" tag="a" class="text-muted">
                <u>Forgot Password?</u>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import { apiService } from "@/common/api.service.js";

export default {
  metaInfo: {
    title: "SignIn"
  },
  data() {
    return {
      username: '',
      password: '',
      userId: "",
      message: '',
      bgImage: require("@/assets/images/photo-wide-4.jpg"),
      logo: require("@/assets/evi_logo_sq.png"),
      signInImage: require("@/assets/images/photo-long-3.jpg")
    };
  },
  mounted() {
    // document.cookie = "csrftoken=;";
    // this.deleteCookie('csrftoken', '', -1);
  },
  computed: {
    validation() {
      return this.userId.length > 4 && this.userId.length < 13;
    },
    ...mapGetters(["loggedInUser", "loading", "error"])
  },

  methods: {
    ...mapActions(["loginDjango"]),

    formSubmit() {
      this.loginDjango({ username: this.username, password: this.password });
    },

    makeToast(variant = null, msg) {
      this.$bvToast.toast(msg, {
        title: ` ${'variant' || "default"}`,
        variant: variant,
        solid: true
      });
    },
    deleteCookie(csrftoken, value, days) {
      var d = new Date;
      d.setTime(d.getTime() + 24*60*60*1000*days);
      document.cookie = csrftoken + "=" + value  + ";path=/;expires=" + d.toGMTString();
    }
  },
  watch: {
    loggedInUser(val) {
      if (val && val.uid && val.uid.length > 0) {
        this.makeToast("success", "Successfully Logged In");

        setTimeout(() => {
          this.$router.push("/");
        }, 500);
      }
    },
    error(val) {
      if (val != null) {
        this.makeToast("warning", val.message);
      }
    }
  },

};
</script>

<style>
.spinner.sm {
  height: 2em;
  width: 2em;
}
</style>
