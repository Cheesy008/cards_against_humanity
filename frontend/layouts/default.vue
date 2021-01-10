<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-toolbar-title style="margin-right: 50px" v-text="title"/>
      <v-spacer></v-spacer>
      <v-btn
        text
        rounded
        to="/"
      >
        Главная
      </v-btn>

      <v-menu
        v-if="$auth.loggedIn"
        offset-y
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
            class="ml-5 mr-5"
          >
            <v-icon large>mdi-account</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="(item, index) in accountListItems"
            :key="index"
            @click="item.action"
            link
          >
            <v-list-item-title v-text="item.title"></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-btn
        v-else
        text
        rounded
        to="/auth/login"
      >
        Войти
      </v-btn>

    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      title: 'Cards against humanity',
      accountListItems: [
        {title: 'Профиль', action: () => this.$router.push({name: 'profile'})},
        {title: 'Выйти', action: () => this.$auth.logout()},
      ]
    }
  },
  methods: {
  }
}
</script>
