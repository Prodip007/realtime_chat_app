<template>
  <div class="login-page">
    <section>
      <div class="container">
        <h1 class="text-center">Welcome to Chatire!</h1>
        <div id="auth-container" class="row">
          <div class="col-sm-4 offset-sm-4">
            <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
              <li class="nav-item">
                <a class="nav-link active" id="signup-tab" data-toggle="tab" href="#signup" role="tab" aria-controls="signup" aria-selected="true"
                  >Sign Up</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" id="signin-tab" data-toggle="tab" href="#signin" role="tab" aria-controls="signin" aria-selected="false"
                  >Sign In</a
                >
              </li>
            </ul>

            <div class="tab-content" id="myTabContent">
              <div class="tab-pane fade show active" id="signup" role="tabpanel" aria-labelledby="signin-tab">
                <form @submit.prevent="signUp">
                  <div class="form-group">
                    <input v-model="email" type="email" class="form-control" id="userEmail" placeholder="Email Address" required />
                  </div>
                  <div class="form-row">
                    <div class="form-group col-md-6">
                      <input v-model="username" type="text" class="form-control" id="userName" placeholder="Username" required />
                    </div>
                    <div class="form-group col-md-6">
                      <input v-model="password" type="password" class="form-control" id="userPassword" placeholder="Password" required />
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" id="toc" required />
                      <label class="form-check-label" for="gridCheck"> Accept terms and Conditions </label>
                    </div>
                  </div>
                  <button type="submit" class="btn btn-block btn-primary">Sign up</button>
                </form>
              </div>

              <div class="tab-pane fade" id="signin" role="tabpanel" aria-labelledby="signin-tab">
                <form @submit.prevent="signIn">
                  <div class="form-group">
                    <input v-model="username" type="text" class="form-control" id="username" placeholder="Username" required />
                  </div>
                  <div class="form-group">
                    <input v-model="password" type="password" class="form-control" id="password" placeholder="Password" required />
                  </div>
                  <button type="submit" class="btn btn-block btn-primary">Sign in</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
export default {
  data() {
    return {
      email: "",
      username: "",
      password: "",
    };
  },
  methods: {
    signUp() {
      console.log("Sign Up");

      let credentials = {
        email: this.email,
        username: this.username,
        password: this.password,
      };

      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
      };

      fetch("http://localhost:8000/auth/users/", options)
      .then((result) => {
        alert("Your account has been created. You will be signed in automatically")
        this.signIn();
      }
      );
    },
    signIn() {
      let credentials = {
        username: this.username,
        password: this.password,
      };

      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
      };

      fetch("http://localhost:8000/auth/token/login/", options)
        .then((result) => result.json())
        .then((data) => {
          localStorage.setItem("authToken", data.auth_token);
          localStorage.setItem("username", this.username);
        })
        .then((data) => {
          if(localStorage.authToken != "undefined") {
            this.$router.push("chats/");
          } else {
            alert("Credentials are not accurate", data)
          }
        });
    },
  },
};
</script>
<style>
.signin-form-wrapper {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
#auth-container {
  margin-top: 50px;
}

.tab-content {
  padding-top: 20px;
}
</style>
