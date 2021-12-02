import firebase from 'firebase/compat/app'
import 'firebase/compat/auth'
import 'firebase/compat/firestore'
import Vue from 'vue'
import { firestorePlugin } from 'vuefire'

Vue.use(firestorePlugin)

const firebaseApp = firebase.initializeApp({
  // ここにfirebaseのapi情報をコピペします.
  apiKey: process.env.FIREBASE_API_KEY,
  authDomain: 'ex-sample-88da3.firebaseapp.com',
  projectId: 'ex-sample-88da3',
  storageBucket: 'ex-sample-88da3.appspot.com',
  messagingSenderId: '121359154811',
  appId: '1:121359154811:web:be9cdad121e2f283f8acde',
  measurementId: 'G-NZYE8WNNJW'
})

export const db = firebaseApp.firestore()
