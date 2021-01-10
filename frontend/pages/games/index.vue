<template>
  <v-app>
    <v-card width="500" class="mx-auto mt-5">
      <v-card-title>
        <h1 class="display-1">Создание игры</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="form.name"
            label="Название комнаты"
          />
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn
              color="info"
              class="mt-3"
              type="submit"
              @click.prevent="createNewGame">Создать
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>

  </v-app>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: ''
      }
    }
  },
  methods: {
    createNewGame() {
      this.$axios.post('game/', {name: this.form.name})
        .then(res => this.$router.push({name: 'games-id', params: {'id': res.data.id}}))
        .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>

</style>
