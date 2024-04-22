<template lang="pug">
    v-row.justify-center
        .border.width-card.pa-10
            div.cat-item(v-for='(item, i) in items' :key='i')
               v-img.img(:src='item.icon' max-width="40")
               span.text-small.text-center {{ item.text }}
</template>
<script>
const MobileCategories = {
    props: {
        title: {default: ''},
        selectedItem: {default: 0},
        items: {default: () => [] }
    },
    data() {
        return {}
    }
}

export default MobileCategories
</script>
<style scoped lang="sass">
.border
    //border-radius: 15px
    display: flex
    overflow-x: auto
.cat-item
    float: left
    width: 80px
.text-small
    font-size: 10px
.img
    margin: auto
    justify-content: center
</style>
