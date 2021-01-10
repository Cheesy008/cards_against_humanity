<template>
  <v-container>
    <v-row
      justify="start"
      align="start"
    >
      <v-col
        v-for="(game, index) in gameList"
        :key="index"
        md="4"
      >
        <v-card
          class="mx-auto"
          width="600"
          outlined
        >
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">
                {{ game.creator_name }}
              </div>
              <v-list-item-title class="headline mb-1">
                {{ game.name }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-card-actions>
            <v-btn
              outlined
              text
              @click="() => $router.push({name: 'games-id', params: {id: game.id}})"
            >
              Войти
            </v-btn>
            <v-btn
              depressed
              color="error"
              @click="$store.dispatch('game/DELETE_GAME_LIST', game.id)"
            >
              Удалить
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "CardItems",
  props: {
    gameList: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {}
  }
}
</script>

<style scoped>

</style>
