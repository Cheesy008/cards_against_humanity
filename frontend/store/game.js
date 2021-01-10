export const state = () => ({
  list: []
})

export const getters = {
  getGameList: state => state.list
}

export const mutations = {
  SAVE_GAME_LIST(state, payload) {
    state.list = payload
  }
}

export const actions = {
  async FETCH_GAME_LIST({commit}) {
    await this.$axios.get('game/')
      .then(res => commit('SAVE_GAME_LIST', res.data))
      .catch(err => console.log(err))
  },
  async DELETE_GAME_LIST({dispatch}, id) {
    await this.$axios.delete(`game/${id}`)
      .then(() => dispatch('FETCH_GAME_LIST'))
      .catch(err => console.log(err))
  },
  async SOCKET_NEW_MESSAGE(ctx, data) {
    console.log('Message:', data)
  }
}
