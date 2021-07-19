<template>
  <li v-bind:style="{'padding-left': (this.node.level-1)*10 + '%',
                      'background-color': (this.bgColor)
                        }"
      v-on:click="changeActive()">
    {{ this.node.value }}
  </li>
</template>

<script>

export default {
  name: 'Node',
  props: {
    node: Object,
  },
  methods: {
    changeActive: function () {
      this.node.is_selected = !this.node.is_selected
      this.$emit('selected', this.node.node_id)
    }
  },
  computed: {
    bgColor: function () {
      var clr = null
      if (this.node.is_selected) {
        clr = 'lightskyblue'
      } else if (this.node.is_deleted) {
        clr = 'indianred'
      } else if (this.node.is_new) {
        clr = 'greenyellow'
      } else if (this.node.is_edited) {
        clr = 'yellow'
      } else {
        clr = 'lightgray'
      }
      return clr
    }

  }
}
</script>

<style>
li {
  list-style-type: None;
  background: mintcream;
  margin-left: 5px;
  padding: 0;
}

ul {
  width: 180px;
}
</style>