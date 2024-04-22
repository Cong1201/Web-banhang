<template lang="pug">
  div
    div.btn.pa-2(@click="$emit('change-value','-')")
      span -
    div.input.pa-2 {{value}}
    div.btn.pa-2(@click="$emit('change-value','+')")
      span +
</template>

<script>
const FastInputQuantity = {
  props: ['value']

}
export default FastInputQuantity
</script>

<style scoped lang="sass">
.btn
  width: 40px
  border: 2px solid #f57e2e
  float: left
  text-align: center
  cursor: point
.input
  width: 80px
  border: 2px
  float: left
  text-align: right
</style>