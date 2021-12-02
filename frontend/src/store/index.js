import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)
const initialState = {
  loginState: {
    id: '',
    token: '',
    isLogin: false
  }
}
export default new Vuex.Store({
  state: initialState,
  mutations: {
    updateLoginState (state, data) {
      state.loginState.id = data.id
      state.loginState.token = data.token
      if (state.loginState.token) {
        console.log('works')
        state.loginState.isLogin = true
        console.log(state.loginState.isLogin)
      }
    },
    logout (state, isLogout) {
      if (isLogout) {
        state.loginState.userId = ''
        state.loginState.userToken = ''
        state.loginState.isLogin = false
      }
    }
  },
  actions: {},
  modules: {},
  plugins: [createPersistedState({ storage: window.sessionStorage })]
})
