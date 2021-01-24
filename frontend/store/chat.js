export const state = () => ({
  messages: [],
})

export const getters = {
}

export const mutations = {
  PUSH_MESSAGE(state, message) {
    state.messages.push(message)
  }
}

export const actions = {
}
