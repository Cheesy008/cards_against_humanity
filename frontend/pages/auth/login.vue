<template>
  <v-app>
    <v-card width="500" class="mx-auto mt-5">
      <v-card-title>
        <h1 class="display-1">Вход</h1>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="form.username"
            label="Никнейм"
            prepend-icon="mdi-account-circle"
          />
          <v-text-field
            v-model="form.password"
            :type="showPassword ? 'text' : 'password'"
            @click:append="showPassword = !showPassword"
            label="Пароль"
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' :'mdi-eye-off'"
          />
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn
              color="info"
              class="mt-3"
              type="submit"
              @click.prevent="login">Войти</v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>

  </v-app>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      form: {
        username: null,
        password: null,
      },
      showPassword: false
    }
  },
  methods: {
    login() {
      this.$auth.loginWith('local', {data: this.form})
      .then(() => {
        this.$router.push({name: 'index'})
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>

</style>
