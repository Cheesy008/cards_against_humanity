<template>
  <v-layout
    column
  >
    <v-flex
      xs12
      sm8
      md6
    >
      <v-btn
        class="mx-2"
        fab
        dark
        color="indigo"
        @click="$router.push({name: 'games'})"
      >
        <v-icon dark>
          mdi-plus
        </v-icon>
      </v-btn>
      <CardItems
        :game-list="gameList"
      />
    </v-flex>
  </v-layout>
</template>

<script>
import CardItems from "@/components/CardItems";
import {mapGetters} from "vuex";

export default {
  components: {
    CardItems
  },
  data() {
    return {}
  },
  computed: {
    ...mapGetters({
      gameList: 'game/getGameList'
    })
  },
  sockets: {
    connect() {
      console.log('connected')
    }
  },
  async fetch({store}) {
    await store.dispatch('game/FETCH_GAME_LIST')
  }
}
</script>
