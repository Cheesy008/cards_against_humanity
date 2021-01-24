<template>
  <v-layout align-center justify-end>
    <v-flex xs12 sm8 md4>
      <v-card class="elevation-12" color="primary lighten-4">
        <v-toolbar dark color="primary darken-1">
          <v-toolbar-title>Чат</v-toolbar-title>
        </v-toolbar>
        <v-card-text>
          <v-list style="height: 400px" ref="chat" id="logs">
            <template v-for="(message, index) in messages">
              <v-subheader v-if="message" :key="index">
                {{printUserMessage(message)}}
              </v-subheader>
            </template>
          </v-list>
        </v-card-text>
        <v-card-actions style="justify-content: center">
          <v-form>
            <div class="wrapper">
              <v-text-field single-line v-model="msg" label="Текст сообщения" style="margin-right: 10px"></v-text-field>
              <v-btn @click.prevent="submitMessage" color="primary" type="submit">Сказать</v-btn>
            </div>
          </v-form>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      messages: [],
      msg: '',
      socket: null
    }
  },
  methods: {
    printUserMessage(message) {
      return `${this.currentTimeFormatted} [${this.$auth.user.username}] ${message}`
    },
    submitMessage() {
      this.socket.send(JSON.stringify({'message': this.msg, 'room_id': this.$route.params.id}))
      this.msg = ''
    },
    connect() {
      this.socket = new WebSocket(
        `ws://localhost:4000/api/v1/chat/ws/${this.$route.params.id}/${this.$auth.user.username}`
      )

      this.socket.onmessage = (event) => {
        console.log(event)
        const data = JSON.parse(event.data)
        this.messages.push(data['text'])
      }

      // this.socket.onopen = (event) => {
      //   this.messages.push(`Игрок ${this.$auth.user.username} присоединился к игре`)
      //   console.log(event, 'Connected')
      // }
      //
      // this.socket.onclose = (event) => {
      //   this.messages.push(`Игрок ${this.$auth.user.username} вышел из игры`)
      // }
    },
  },
  computed: {
    currentTimeFormatted() {
      const time = new Date();
      return `${time.getHours()}:${time.getMinutes()}`
    }
  },
  mounted() {
    this.connect()
  }
}
</script>

<style scoped lang="scss">
#logs {
  height: 100px;
  overflow: auto;
}

.wrapper {
  display: flex;
  align-items: center;
}
</style>
