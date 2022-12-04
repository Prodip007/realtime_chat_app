<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-6 offset-3">
        <div v-if="sessionStarted" id="chat-container" class="card">
          <div class="card-header text-white text-center font-weigth-bold subtle-blue-gradient">Share this page url to invite new friends</div>
          <div class="card-body">
            <div class="container chat-body">
              <div class="row chat-session">
                <div class="col-sm-2">
                  <img class="rounded-circle" src="http://placehold.it/40/f16000/fff&text=D" alt="" />
                </div>
                <div class="col-sm-7">
                  <span class="card-text speech-bubble speech-bubble-peer">Hello!</span>
                </div>
              </div>
              <div class="row chat-section">
                <div class="col-sm-7 offset-3">
                  <span class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient"> Whatsup, another chat app? </span>
                </div>
                <div class="col-sm-2">
                  <img class="rounded-circle" src="http://placehold.it/40/333333/fff&text=A" />
                </div>
              </div>
              <div class="row chat-section">
                <div class="col-sm-2">
                  <img class="rounded-circle" src="http://placehold.it/40/f16000/fff&text=D" />
                </div>
                <div class="col-sm-7">
                  <p class="card-text speech-bubble speech-bubble-peer">
                    Yes this is Chatire, it's pretty cool and it's Open source and it was built with Django and Vue JS so we can tweak it to our satisfaction.
                  </p>
                </div>
              </div>
              <div class="row chat-section">
                <div class="col-sm-7 offset-3">
                  <p class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">Okay i'm already hacking around let me see what i can do to this thing.</p>
                </div>
                <div class="col-sm-2">
                  <img class="rounded-circle" src="http://placehold.it/40/333333/fff&text=A" />
                </div>
              </div>
            </div>
          </div>
          <div class="card-footer text-muted">
            <form>
              <div class="row">
                <div class="col-sm-10">
                  <input type="text" placeholder="Type a message" />
                </div>
                <div class="col-sm-2">
                  <button class="btn btn-primary">Send</button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div v-else>
          <h3 class="text-center">Welcome!</h3>
          <br />
          <p class="text-center">To start chatting with friends click on the button below, it'll start a new chat session and then you can invite your friends over to chat!</p>
          <br />
          <button @click="startChatSession" class="btn btn-primary btn-lg btn-block">Start Chatting</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      sessionStarted: false,
      auth_token: null,
    };
  },
  created() {
    this.username = localStorage.getItem("username");
    this.auth_token = localStorage.getItem("authToken");
    // console.log(localStorage)
  },
  methods: {
    startChatSession() {
      this.sessionStarted = true;
      this.$router.push("/chats/chat_url/");
    },
    
    startChatSession() {
      console.log(this.auth_token)
      let options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          'Authorization': `Token ${this.auth_token}`

        },
        body: JSON.stringify(this.locationData),
      };
      fetch('http://localhost:8000/api/chats/', options)
      .then((result) => result.json())
      .then((data) => {
        console.log('A new session has been created')
        this.sessionStarted = true
        this.$router.push(`/chats/${data.uri}`)
      })
    },
  },
};
</script>
<style lang="scss">
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}

.btn {
  border-radius: 0 !important;
}

.card-footer input[type="text"] {
  background-color: #ffffff;
  color: #444444;
  padding: 7px;
  font-size: 13px;
  border: 2px solid #cccccc;
  width: 100%;
  height: 38px;
}

.card-header a {
  text-decoration: underline;
}

.card-body {
  background-color: #ddd;
}

.chat-body {
  margin-top: -15px;
  margin-bottom: -5px;
  height: 380px;
  overflow-y: auto;
}

.speech-bubble {
  display: inline-block;
  position: relative;
  border-radius: 0.4em;
  padding: 10px;
  background-color: #fff;
  font-size: 14px;
}

.subtle-blue-gradient {
  background: linear-gradient(45deg, #004bff, #007bff);
}

.speech-bubble-user:after {
  content: "";
  position: absolute;
  right: 4px;
  top: 10px;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  border-left-color: #007bff;
  border-right: 0;
  border-top: 0;
  margin-top: -10px;
  margin-right: -20px;
}

.speech-bubble-peer:after {
  content: "";
  position: absolute;
  left: 3px;
  top: 10px;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  border-right-color: #ffffff;
  border-top: 0;
  border-left: 0;
  margin-top: -10px;
  margin-left: -20px;
}

.chat-section:first-child {
  margin-top: 10px;
}

.chat-section {
  margin-top: 15px;
}

.send-section {
  margin-bottom: -20px;
  padding-bottom: 10px;
}
</style>
