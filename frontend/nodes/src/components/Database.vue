<template>
  <div>
    <h2>Database</h2>
    <br>
    <div class="buttons">
      <button v-on:click="$emit('addToCacheEvent')">Add to Cache</button>
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
  name: 'Database',
  components: {Node},
  props: ['nodes', 'dbComponentKey'],
  data() {
    return {
      mutableNodes: this.nodes,
      mutableDBComponentLey: this.dbComponentKey
    }
  },
  methods: {
    changeActive: function (node) {
      this.$emit('changeActiveNodeDB', 'changeActiveNodeDB', node)
    }
  },
  created() {
    this.$emit('getAllNodes')
  },
}
</script>

<style>
ul {
  list-style-type: square;
  list-style-position: inside;
  position: center;
  padding-left: 5px;
  padding-right: 5px;
}
</style>