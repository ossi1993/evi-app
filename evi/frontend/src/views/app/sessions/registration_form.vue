<template>
  <div
    class="auth-layout-wrap"
    :style="{ backgroundImage: 'url(' + bgImage + ')' }"
  >
    <div class="auth-content">
      <div class="card o-hidden">
        <div class="row">
          <b-col md="12">
            <div class="p-5">
              <div class="auth-logo text-center">
                <img :src="logo" alt="" />
              </div>
              <h1 class="mb-3 text-center text-20">Sign Up</h1>
              <b-form @submit.prevent="submit">
                <b-form-group label="Your Name">
                  <b-form-input class="form-control form-control-rounded" label="Name" v-model.trim="$v.fName.$model">
                  </b-form-input>
                  <b-alert show variant="danger" class="error col mt-1" v-if="!$v.fName.minLength">Name must have at least
                    {{ $v.fName.$params.minLength.min }} letters.</b-alert>
                </b-form-group>
                <b-form-group label="Email">
                  <b-form-input class="form-control form-control-rounded" label="Name" type="email" v-model="email">
                  </b-form-input>
                </b-form-group>
                <b-form-group label="Password">
                  <b-form-input class="form-control form-control-rounded" label="Name" type="password" v-model.trim="$v.password.$model">
                  </b-form-input>
                  <b-alert show variant="danger" class="error col mt-1" v-if="!$v.password.minLength">Minimum
                    {{ $v.password.$params.minLength.min }} charaters.</b-alert>
                </b-form-group>
                <b-form-group label="Repeat Password">
                  <b-form-input class="form-control form-control-rounded" label="Name" type="password" v-model.trim="$v.repeatPassword.$model">
                  </b-form-input>
                  <b-alert show variant="danger" class="error col mt-1" v-if="!$v.repeatPassword.sameAsPassword">Passwords must be identical.</b-alert>
                </b-form-group>
                <b-button type="submit" block variant="primary" :disabled="submitStatus === 'PENDING' || $v.$invalid" class="btn-rounded">Sign Up</b-button>
                <b-button to="signIn" block variant="outline-primary mt-2" class="btn-rounded">Sign In</b-button>
                <p v-once class="typo__p" v-if="submitStatus === 'OK'">
                  {{ makeToastTwo("success") }}
                  {{ this.$router.push("/") }}
                </p>
                <p v-once class="typo__p" v-if="submitStatus === 'ERROR'">
                  {{ makeToast("danger") }}
                </p>
                <div v-once class="typo__p" v-if="submitStatus === 'PENDING'">
                  <div class="spinner sm spinner-primary mt-3"></div>
                </div>
              </b-form>
            </div>
          </b-col>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { required, sameAs, minLength } from "vuelidate/lib/validators";
import { mapGetters, mapActions } from "vuex";
export default {
  metaInfo: {
    // if no subcomponents specify a metaInfo.title, this title will be used
    title: "SignUp"
  },

  data() {
    return {
      fName: "",
      email: "",
      bgImage: require("@/assets/images/photo-wide-4.jpg"),
      logo: require("@/assets/evi_logo_sq.png"),
      signInImage: require("@/assets/images/photo-long-3.jpg"),
      password: "",
      repeatPassword: "",
      submitStatus: null
    };
  },

  validations: {
    fName: {
      required,
      minLength: minLength(4)
    },

    password: {
      required,
      minLength: minLength(5)
    },
    repeatPassword: {
      sameAsPassword: sameAs("password")
    }

    // add input
    // peopleAdd: {
    //   required,
    //   minLength: minLength(3),
    //   $each: {
    //     multipleName: {
    //       required,
    //       minLength: minLength(5)
    //     }
    //   }
    // },
    // validationsGroup:['peopleAdd.multipleName']
  },

  computed: {
    ...mapGetters(["loggedInUser", "loading", "error"])
  },

  methods: {
    ...mapActions(["signUserUp"]),
    //   validate form
    submit() {
      console.log("submit!");

      this.$v.$touch();
      if (this.$v.$invalid) {
        this.submitStatus = "ERROR";
      } else {
        this.signUserUp({ email: this.email, password: this.password });
        this.submitStatus = "PENDING";
        setTimeout(() => {
          this.submitStatus = "OK";
        }, 1000);
      }
    },
    makeToast(variant = null) {
      this.$bvToast.toast("Please fill the form correctly.", {
        title: `Variant ${variant || "default"}`,
        variant: variant,
        solid: true
      });
    },
    makeToastTwo(variant = null) {
      this.$bvToast.toast("Successfully Created Account", {
        title: `Variant ${variant || "default"}`,
        variant: variant,
        solid: true
      });
    },

    inputSubmit() {
      console.log("submitted");
    }
  }
};
</script>
<style>
.spinner.sm {
  height: 2em;
  width: 2em;
}
</style>


