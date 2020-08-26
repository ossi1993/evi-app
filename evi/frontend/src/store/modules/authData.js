import firebase from "firebase/app";
import "firebase/auth";
import { apiService } from "@/common/api.service.js";

export default {
  state: {
    loggedInUser:
      localStorage.getItem("userInfo") != null
        ? JSON.parse(localStorage.getItem("userInfo"))
        : null,
    loading: false,
    error: null
  },
  getters: {
    loggedInUser: state => state.loggedInUser,
    loading: state => state.loading,
    error: state => state.error
  },
  mutations: {
    setUser(state, data) {
      state.loggedInUser = data;
      state.loading = false;
      state.error = null;
    },
    setLogout(state) {
      state.loggedInUser = null;
      state.loading = false;
      state.error = null;
      // this.$router.go("/");
    },
    setLoading(state, data) {
      state.loading = data;
      state.error = null;
    },
    setError(state, data) {
      state.error = data;
      state.loggedInUser = null;
      state.loading = false;
    },
    clearError(state) {
      state.error = null;
    }
  },
  actions: {
    loginDjango({commit}, data) {
      commit("clearError");
      commit("setLoading", true);
      let username = data.username;
      let password = data.password;
      let endpoint = `/api/rest-auth/login/`
      apiService(endpoint, "POST", { username, password })
        .then(response => {
          localStorage.setItem("userInfo", JSON.stringify(username));
          commit("setUser", {uid: username});
          console.log("response");
        })
        .catch(function(error) {
          localStorage.removeItem("userInfo");
          commit("setError", error);
        });
    },



    login({commit}, data) {
      commit("clearError");
      commit("setLoading", true);
      firebase
        .auth()
        .signInWithEmailAndPassword(data.email, data.password)
        .then(user => {
          const newUser = {uid: user.user.uid};
          localStorage.setItem("userInfo", JSON.stringify(newUser));
          commit("setUser", {uid: user.user.uid});
          console.log("user");
        })
        .catch(function(error) {
          // Handle Errors here.
          // var errorCode = error.code;
          // var errorMessage = error.message;
          // console.log(error);
          localStorage.removeItem("userInfo");
          commit("setError", error);
          // ...
        });
    },

    signUserUp({commit}, data) {
      commit("setLoading", true);
      commit("clearError");
      firebase
        .auth()
        .createUserWithEmailAndPassword(data.email, data.password)
        .then(user => {
          commit("setLoading", false);

          const newUser = {
            uid: user.user.uid
          };
          console.log(newUser);
          localStorage.setItem("userInfo", JSON.stringify(newUser));
          commit("setUser", newUser);
        })
        .catch(error => {
          commit("setLoading", false);
          commit("setError", error);
          localStorage.removeItem("userInfo");
          console.log(error);
        });
    },
    signOut({commit}) {
      firebase
        .auth()
        .signOut()
        .then(
          () => {
            localStorage.removeItem("userInfo");
            commit("setLogout");
          },
          _error => {}
        );
    }
  }
};
