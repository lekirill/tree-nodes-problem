<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          Node {{ node.node_id }} Value
        </slot>
        <button
            type="button"
            class="btn-close"
            v-on:click="$emit('closeEdit')"
        >
          x
        </button>
      </header>

      <section class="modal-body">
        <slot name="body">
          <input v-model="node.value">
          <button
              type="button"
              v-on:click="$emit('saveEdit', node.node_id, node.value)">Save
          </button>
        </slot>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Edit',
  props: {
    'node': {'node_id': -1, 'value': 'test'}
  }
};
</script>

<style>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #FFFFFF;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
}

.modal-header {
  padding: 15px;
  display: flex;
}

.modal-header {
  position: relative;
  border-bottom: 1px solid #eeeeee;
  color: #4AAE9B;
  justify-content: space-between;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
}

.btn-close {
  position: absolute;
  top: 0;
  right: 0;
  border: none;
  font-size: 20px;
  padding: 10px;
  cursor: pointer;
  font-weight: bold;
  color: #4AAE9B;
  background: transparent;
}

</style>