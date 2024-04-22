<template lang="pug">
    .border.width-card
       v-list(dense='')
          v-subheader {{ title }}
          v-list-item-group(v-model='selectedItem' color='#f57e2e')
            v-list-item(v-for='(item, i) in items' :key='i')
              v-img(:src='item.icon' max-width="25")
              span.pl-4 {{ item.text }}
</template>
<script>
const Categories = {
    props: {
        title: {default: ''},
        selectedItem: {default: 0},
        items: {default: () => [] }
    },
    data() {
        return {}
    }
}

export default Categories
</script>
<style scoped lang="sass">
.border
    //border-radius: 15px
    border: 2px solid #f57e2e
.width-card
    max-width: 250px
</style>
