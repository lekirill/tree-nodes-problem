<template>
  <div>
    <h2>Cache</h2>
    <br>
    <div class="buttons">
      <button v-on:click="$emit('addNewNode')">+</button>
      <button v-on:click="$emit('deleteNodeFromDB')">-</button>
      <button v-on:click="$emit('showEdit')">Edit</button>
      <button v-on:click="$emit('removeFromCache')">RM from Cache</button>
      <button v-on:click="$emit('loadToDB')">Apply</button>
      <button v-on:click="$emit('resetAll')">Reset</button>
    </div>
    <br>
    <ul>
      <Node
          v-for="node in nodes"
          :key="node.node_id"
          v-bind:node="node"
          v-on:selected="changeActive(node)"
      />
    </ul>
  </div>
</template>

<script>
import Node from '@/components/Node'

export default {
  name: 'Cache',
  components: {
    Node
  },
  props: ['nodes', 'cacheComponentKey'],
  data() {
    return {
      mutableNodes: this.nodes,
      mutableCacheComponentKey: this.cacheComponentKey
    }
  },
  methods: {
    changeActive: function (node) {
      this.$emit('changeActiveNodeCache', 'changeActiveNodeCache', node)
    }
  },
  created() {
    this.$emit('getCache')
  },

}
</script>

<style>
.buttons {
  height: 20px;
  align-content: center;
  text-align: center;
}
</style>