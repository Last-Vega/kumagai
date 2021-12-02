<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="1000">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">
          タスク説明
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          表示される文献を，各々の文献管理の基準に基づいて好きな位置に配置してもらいます
        </v-card-title>

        <v-card-text>
          <ol>
            <li>
              一つ目の文献が座標平面上の(0,0)の位置にプロットされています．その文献の情報は画面左下の表「動かす文献」から確認できます．その情報をもとに，適当な位置を決めて動かしてください．プロットされた点はドラッグ操作動かすことができます．
            </li>
            <li>
              位置が確定したら，画面左下の「次の文献を動かす」ボタンを押してください．
            </li>
            <li>
              新たな文献が座標平面上の(0,0)の位置にプロットされます．画面左下の表「動かす文献」を確認しながら文献を適当な位置に配置してください
            </li>
            <li>
              これまでに動かした文献は，赤色でプロットされた各点をホバーすることで画面右下の表「マウスがホバーした文献」から確認することができます．これまでに動かした文献も，同様にドラッグ操作で動かすことだできます．
            </li>
            <li>
              「実験は終了です」というアラートが出たら実験は終わりになります．
            </li>
          </ol>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">
            確認しました
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: 'taskInstraction',
  data () {
    return {
      dialog: false
    }
  }
}
</script>
