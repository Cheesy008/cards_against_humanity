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
                {{printMessage(message)}}
              </v-subheader>
            </template>
          </v-list>
        </v-card-text>
        <v-card-actions style="justify-content: center">
          <v-form>
            <div class="wrapper">
              <v-text-field single-line v-model="messageText" label="Текст сообщения" style="margin-right: 10px"></v-text-field>
              <v-btn @click.prevent="submitMessage" color="primary" type="submit">Сказать</v-btn>
            </div>
          </v-form>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import {MessageType} from "@/utils/enums";
import moment from "moment";

import {mapState, mapMutations} from 'vuex'

export default {
  data() {
    return {
      messageText: '',
      socket: null
    }
  },
  methods: {
    ...mapMutations({
      pushMessage: "chat/PUSH_MESSAGE"
    }),
    printMessage(message) {
      const messageText = message['message_text']
      const date = moment(message['date']).format('h:mm')
      const username = message['username']
      const messageType = message['message_type']

      const userMessage = `${date} [${username}] ${messageText}`
      const gameMessage = `${date} ${messageText}`

      return messageType == MessageType.MESSAGE ? userMessage :gameMessage
    },
    submitMessage() {
      this.socket.send(JSON.stringify({'message_text': this.messageText}))
      this.messageText = ''
    },
    websocketConnect() {
      this.socket = new WebSocket(
        `ws://localhost:4000/ws/${this.$route.params.id}/${this.$auth.user.username}`
      )

      this.socket.onmessage = (event) => {
        console.log(event)
        const data = JSON.parse(event.data)
        this.pushMessage(data['message'])
      }

    },
  },
  computed: {
    ...mapState('chat', {
      messages: state => state.messages
    })
  },
  mounted() {
    this.websocketConnect()
  },
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
