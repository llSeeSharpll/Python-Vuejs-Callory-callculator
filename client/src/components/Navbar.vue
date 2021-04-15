<template>
  <div>
    <b-navbar toggleable="lg" variant="light" type="light">
      <b-navbar-brand
        ><router-link :to="{ name: 'home' }" class="navbar-brand"
          >Callory Calculator</router-link
        ></b-navbar-brand
      >

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item
            v-if="getIsUserLoggedIn == undefined || getIsUserLoggedIn == false"
            ><router-link class="text-dark" :to="{ name: 'login' }"
              >Log in</router-link
            ></b-nav-item
          >
          <b-nav-item
            v-if="getIsUserLoggedIn == undefined || getIsUserLoggedIn == false"
          >
            <router-link class="text-dark" :to="{ name: 'register' }"
              >Register</router-link
            ></b-nav-item
          >
          <b-nav-item class="font-wieght-bold" v-if="getIsUserLoggedIn == true">
            <router-link class="text-dark" :to="{ name: 'home' }">
              {{ username }}
            </router-link>
          </b-nav-item>
          <b-button
            v-if="getIsUserLoggedIn"
            @click="processLogout()"
            variant="light"
            type="light"
          >
            Logout
          </b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
export default {
  Name: "Navbar",
  data() {
    return {
      username: sessionStorage.getItem("username"),
    };
  },
  computed: {
    ...mapGetters(["getIsUserLoggedIn"]),
  },
  methods: {
    ...mapActions(["logout"]),
    processLogout() {
      this.logout({ controllerReference: this }).then(function (ctrl) {
        window.location.reload();
        ctrl.$router.push("/login");
      });
    },
  },
};
</script>