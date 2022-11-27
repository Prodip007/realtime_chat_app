<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
    <span v-if="logged_in">| <a @click="logOut">Logout</a></span>

  </nav>
  <router-view />
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;
    cursor: pointer;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
<script>
export default {
  data() {
    return {
      logged_in: false
    }

  },
  methods: {
    logOut() {
      localStorage.removeItem("authToken");
      this.$router.go()
      this.$router.push("/auth");
    },

    loggedInOrNot() {
      if (localStorage.authToken) {
        this.logged_in = true
      }
    },
  },

  created() {
    this.$watch(
      () => this.$route.params,
      () => {
        this.loggedInOrNot()
      },
      {
        immediate: true
      }
    )
  }
};
</script>
