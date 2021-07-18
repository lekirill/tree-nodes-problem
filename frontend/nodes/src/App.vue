<template>
  <div id="app">
    <div>
      <div class="container" id="cache">
        <Cache v-bind:nodes="this.cache_nodes"
               v-on:getCache="getCache"
               v-on:changeActiveNodeCache="changeSelected"
               v-on:removeFromCache="removeFromCache"
               v-on:addNewNode="addNewNode"
               v-on:deleteNodeFromDB="deleteNodeFromDB"
               v-on:loadToDB="loadToDB"
               v-on:resetAll="resetAll"
               v-on:showEdit="showEdit"
               v-bind:key="cacheComponentKey"
        ></Cache>
      </div>
      <div class="container" id="database">
        <Database v-bind:nodes="this.db_nodes"
                  v-on:addToCacheEvent="addToCache"
                  v-on:changeActiveNodeDB="changeSelected"
                  v-on:getAllNodes="getAllNodes"
                  v-bind:key="dbComponentKey"
        >
        </Database>
      </div>
    </div>
    <Edit
        v-if="this.selected_node !== null"
        v-on:closeEdit="closeEdit"
        v-on:saveEdit="saveEdit"
        v-show="this.isEditVisible"
        v-bind:node="this.selected_node"
    />
  </div>

</template>

<script>

import Cache from '@/components/Cache'
import Database from '@/components/Database'
import Edit from '@/components/Edit';
import axios from "axios";

export default {
  name: 'App',
  data() {
    return {
      db_nodes: [],
      cache_nodes: [],
      selected_node: null,
      selection_type: null,
      cacheComponentKey: 0,
      dbComponentKey: 0,
      isEditVisible: false
    }
  },
  components: {
    Cache,
    Database,
    Edit
  },
  methods: {
    addToCache: function () {
      if (this.selected_node !== null && this.selection_type === 'changeActiveNodeDB') {
        var node = this.db_nodes.filter(t => t.node_id === this.selected_node.node_id)[0]
        let axiosConfig = {
          headers: {
            'Content-Type': 'application/json;charset=UTF-8'
          }
        }
        axios
            .post('http://localhost:8000/v1/nodes/add', {'node_id': node.node_id}, axiosConfig)
            .then((response) => {
              console.log(response.data)
            })
        this.selected_node = null
        this.getCache()
        this.cacheForceRerender()
        window.location.reload();
      }
    },
    loadToDB: function () {
      this.cacheForceRerender()
      let axiosConfig = {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8'
        }
      }
      axios
          .post('http://localhost:8000/v1/nodes/update', this.cache_nodes, axiosConfig)
          .then((response) => {
            console.log(response.data)
          })
      this.getCache()
      this.cacheForceRerender()
      this.dbForceRerender()
      this.selected_node = null
      window.location.reload();
    },
    resetAll: function () {
      this.cacheForceRerender()
      let axiosConfig = {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8'
        }
      }
      axios
          .post('http://localhost:8000/v1/nodes/reset', this.cache_nodes, axiosConfig)
          .then((response) => {
            console.log(response.data)
          })
      this.getCache()
      this.cacheForceRerender()
      this.dbForceRerender()
      this.selected_node = null
      window.location.reload();
    },
    removeFromCache: function () {
      this.cacheForceRerender()
      if (this.selected_node !== null && this.selection_type === 'changeActiveNodeCache') {
        let axiosConfig = {
          headers: {
            'Content-Type': 'application/json;charset=UTF-8'
          }
        }
        var node = this.cache_nodes.filter(t => t.node_id === this.selected_node.node_id)[0]
        axios
            .post('http://localhost:8000/v1/cache/remove', {'node_id': node.node_id}, axiosConfig)
            .then((response) => {
              console.log(response.data)
            })
        this.getCache()
        this.cacheForceRerender()
        this.selected_node = null
      }
    },
    deleteNodeFromDB: function () {
      this.cacheForceRerender()
      if (this.selected_node !== null && this.selection_type === 'changeActiveNodeCache') {
        let axiosConfig = {
          headers: {
            'Content-Type': 'application/json;charset=UTF-8'
          }
        }
        var node = this.db_nodes.filter(t => t.node_id === this.selected_node.node_id)[0]
        console.log(node.node_id)
        axios
            .post('http://localhost:8000/v1/cache/del', {'node_id': node.node_id}, axiosConfig)
            .then((response) => {
              console.log(response.data)
            })
        this.getCache()
        this.cacheForceRerender()
        this.selected_node = null
      }
    },
    getAllNodes: function () {
      this.cacheForceRerender()
      axios
          .get('http://localhost:8000/v1/nodes/')
          .then((response) => {
            response.data.flat_tree.forEach((node) => {
                  node.is_selected = false
                }
            )
            this.db_nodes = response.data.flat_tree
          })
      this.cacheForceRerender()
    },
    addNewNode: function () {
      if (this.selected_node !== null && this.selection_type === 'changeActiveNodeCache') {
        var node = this.cache_nodes.filter(t => t.node_id === this.selected_node.node_id)[0]
        console.log(node)
        let axiosConfig = {
          headers: {
            'Content-Type': 'application/json;charset=UTF-8'
          }
        }
        axios
            .post('http://localhost:8000/v1/cache/add', {'parent_id': node.node_id}, axiosConfig)
            .then((response) => {
              console.log(response.data)
              this.cache_nodes = response.data.flat_tree
            })

        this.cacheForceRerender()
        this.selected_node = null
      }

    },
    saveEdit: function (node_id, value) {

      axios
          .post('http://localhost:8000/v1/cache/save',  {'node_id': node_id, 'value': value})
          .then((response) => {
            console.log(response.data)
            this.cache_nodes = response.data.flat_tree
          })
      this.cacheForceRerender()
      this.selected_node = null
      this.closeEdit()
    },
    showEdit: function () {
      if (this.selected_node !== null && this.selection_type === 'changeActiveNodeCache') {
        console.log('show')
        this.isEditVisible = true
      }
    },
    closeEdit: function () {
      console.log('close')
      this.isEditVisible = false
    },
    getCache: function () {
      axios
          .get('http://localhost:8000/v1/cache/')
          .then((response) => {
            response.data.flat_tree.forEach((node) => {
                  node.is_selected = false
                }
            )
            this.cache_nodes = response.data.flat_tree
          })
    },
    changeSelected: function (event, node) {
      var do_rerender = false
      if (event !== this.selection_type) {
        do_rerender = true
      }
      this.selected_node = node
      this.selection_type = event
      if (event === 'changeActiveNodeCache') {
        if (do_rerender) {
          this.dbForceRerender()
        }
        this.cache_nodes.forEach(n => {
          if (n.node_id !== this.selected_node.node_id) {
            n.is_selected = false
          } else {
            n.is_selected = true
          }
        })
        this.db_nodes.forEach(n => {
              n.is_active = false
            }
        )
      }
      if (event === 'changeActiveNodeDB') {
        if (do_rerender) {
          this.cacheForceRerender()
        }
        this.db_nodes.forEach(n => {
          if (n.node_id !== this.selected_node.node_id) {
            n.is_selected = false
          } else {
            n.is_selected = true
          }
        })
        this.cache_nodes.forEach(n => {
              n.is_active = false
            }
        )
      }
    },
    cacheForceRerender() {
      this.cacheComponentKey += 1
    },
    dbForceRerender() {
      this.dbComponentKey += 1
    },
  },
  created() {
    this.getAllNodes()
    this.getCache()
    this.cacheForceRerender()
    this.dbForceRerender()

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  width: 500px;
}

.container {
  display: inline-flex;
  flex-direction: row;
  text-align: left;
  width: 40%;
}

#cache {
  background: whitesmoke;
  margin: 5%;
}

#database {
  background: whitesmoke;
  margin: 5%;
}

h2 {
  text-align: center;
}
</style>
