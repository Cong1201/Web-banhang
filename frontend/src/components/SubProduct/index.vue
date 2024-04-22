<template lang="pug">
  .max-width-product-component.float-left(@click="onClick()")
    v-img.max-width-product-component(:src="product.img")
    .product-name.align-left
        span {{product.name}}
    .product-review.align-left
        span {{product.star}}
        v-icon(color="#f57e2e") mdi-star
        span {{product.sales}}
    .price.align-left
        h4 {{product.price}} đ
    .cmt.align-left {{product.cmt}}
    v-divider
    .cmt.align-left {{product.shipCmt}}
</template>
<script>
import router from '@/router'

const SubProduct = {
    props: ['product'],
    methods: {
      onClick() {
        router.push({
          path: '/product_detail'
        })
      }
    }
}

export default SubProduct
</script>

<style scoped lang="sass">
.max-width-product-component
    max-width: 200px
.align-left
    text-align: left
.price
    font-size: 20px
.cmt
    font-size: 12px
    color: gray
.float-left
    float:left
</style>
