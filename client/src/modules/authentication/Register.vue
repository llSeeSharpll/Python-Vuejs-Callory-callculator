<template>
  <div class="mt-5 text-left d-inline-block">
    <h1>Register</h1>
    <form class="font-weight-bold">
      <div class="mx-1">Name</div>
      <input
        name="email"
        label="Email*"
        class="rounded"
        v-model="username"
        prepend-icon="mdi-account-circle"
        required
      /><br />
      <div class="mx-1">Email</div>
      <input
        class="rounded"
        name="email"
        label="Email*"
        v-model="email"
        prepend-icon="mdi-account-circle"
        required
        :rules="[checkIsRequired(email), validateEmail(email)]"
        type="email"
      /><br />
      <div class="mx-1">Password</div>
      <input
        class="rounded"
        name="password"
        label="Password*"
        v-model="password"
        :type="getPasswordFieldType()"
        prepend-icon="mdi-lock"
        :append-icon="getShowPasswordApendIcon()"
        @click:append="toggleShowPassword()"
        counter="50"
        required
        :rules="[checkIsRequired(password), checkMinLenght(password.length, 8)]"
        loading
      /><br />
      <div class="mx-1">Mobile Phone Number</div>
      <input
        name="mobilePhone"
        label="Mobile Phone"
        class="rounded"
        v-model="mobilePhone"
        prepend-icon="mdi-phone"
        type="tel"
      />
      <div class="mx-1">Weight</div>
      <input
        name="mobilePhone"
        label="Mobile Phone"
        class="rounded"
        v-model="weight"
        prepend-icon="mdi-phone"
        type="tel"
      />
      <div class="mx-1">Height</div>
      <input
        name="mobilePhone"
        label="Mobile Phone"
        class="rounded"
        v-model="height"
        prepend-icon="mdi-phone"
        type="tel"
      />
      <div class="mx-1">Age</div>
      <input
        name="mobilePhone"
        label="Mobile Phone"
        class="rounded"
        v-model="Age"
        prepend-icon="mdi-phone"
        type="tel"
      />
      <div class="mx-1">
        <div>Gender</div>
        <div class="form-check">
          <input
            class="form-check-input"
            value="male"
            type="radio"
            name="flexRadioDefault"
            id="flexRadioDefault1"
            v-model="gender"
          />
          <label class="form-check-label" for="flexRadioDefault1"> Male </label>
        </div>
        <div class="form-check">
          <input
            v-model="gender"
            value="female"
            class="form-check-input"
            type="radio"
            name="flexRadioDefault"
            id="flexRadioDefault2"
            checked
          />
          <label class="form-check-label" for="flexRadioDefault2">
            Female
          </label>
        </div>
      </div>
    </form>
    <div>
      <router-link class="text-dark font-weight-bold" to="login">Go to login</router-link>
      <button
        class="mx-3 btn border-dark"
        @click="
          registerNewUser({
            username: username,
            email: email,
            password: password,
            mobilePhone: mobilePhone,
            gender: gender,
            weight: weight,
            height: height,
            age: age
          }).then(()=>{
            alert.alert('Register Success')
          }).catch(()=>{
            alert.alert('Username or email already used')
          })
        "
      >
        Register
      </button>
    </div>
  </div>
</template>

<script>
import alert from 'vue-simple-alert'
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Register",
  data: function () {
    return {
      showPassword: false,
      isRegisterFormValid: false,
      email: "",
      password: "",
      mobilePhone: "",
      username: "",
      gender: "",
      alert,
      weight:"",
      height:"",
      age:"",
    };
  },
  methods: {
    getPasswordFieldType: function () {
      if (this.showPassword) {
        return "text";
      } else {
        return "password";
      }
    },
    toggleShowPassword: function () {
      this.showPassword = !this.showPassword;
    },
    getShowPasswordApendIcon: function () {
      if (this.showPassword) {
        return "mdi-eye";
      } else {
        return "mdi-eye-off";
      }
    },
    checkIsRequired: function (value, errorMessage) {
      if (!errorMessage) {
        errorMessage = "This field is required";
      }
      return !!value || errorMessage;
    },
    checkMinLenght(valueLenght, minLength, errorMessage) {
      if (!errorMessage) {
        errorMessage = `Min length is ${minLength}`;
      }
      return (!!valueLenght && valueLenght >= minLength) || errorMessage;
    },
    progress(minLength) {
      return Math.min(100, (this.password.length / minLength) * 100);
    },
    color(minLength) {
      let selectedColorIndex = 0;
      if (this.progress(minLength) < 40) {
        selectedColorIndex = 0;
      } else if (
        this.progress(minLength) > 40 &&
        this.progress(minLength) < 100
      ) {
        selectedColorIndex = 1;
      } else {
        selectedColorIndex = 2;
      }
      return ["error", "warning", "success"][selectedColorIndex];
    },
    ...mapActions(["registerNewUser", "setSnackbarVisibility"]),
    validateEmail(email) {
      var re = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
      return (
        re.test(String(email).toLowerCase()) ||
        "Oops, this doesn't looks like rigth, can you check please?"
      );
    },
  },
  computed: {
    ...mapGetters([
      "getIsRegistrationProcessSucceed",
      "getRegistrationProcessMessage",
      "isProcessing",
      "GetIsSnackbarVisible",
    ]),
  },
};
</script>