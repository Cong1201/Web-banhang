<template lang = "pug">
  div
    v-row
      v-col(:cols="screenType === 'pc' ? 4 : (screenType === 'tab' ? 5 : 12)")
        .pa-4
          v-row
            v-col(cols="12")
              v-img(src="https://salt.tikicdn.com/cache/750x750/ts/product/93/b1/7f/dfbc0cdec12ab9c81748a1715beef22a.png.webp")
          v-row
            v-col(cols="3")
              v-img(src="https://salt.tikicdn.com/cache/750x750/ts/product/93/b1/7f/dfbc0cdec12ab9c81748a1715beef22a.png.webp")
            v-col(cols="3")
              v-img(src="https://salt.tikicdn.com/cache/750x750/ts/product/7d/6a/67/3829eda45ebe12a1f2e55c7415ae8c2d.png.webp")
            v-col(cols="3")
              v-img(src="https://salt.tikicdn.com/cache/750x750/ts/product/62/21/fa/aaab14f99fa5b012fa625b3e5c2b570e.png.webp")
            v-col(cols="3")
              v-img(src="https://salt.tikicdn.com/cache/750x750/ts/product/b0/91/13/7bc8d623a5a7123d5d0ca186cb4d52cd.png.webp")
      v-col(:cols="screenType === 'pc' ? 8 : (screenType === 'tab' ? 7 : 12)")
        .pa-4
          p.align-left Thương hiệu: {{product.trademark}}
          h1.align-left {{product.name}}
          p.align-left
            v-icon(v-for="i in product.star" color= "#f57e2e") mdi-star
            span.pa-6 Đã bán: {{product.sales}}
          p.align-left
            del {{product.cost}} đ -->
            span.price {{product.price}} đ
          p.align-left
              span Vận chuyển
              v-icon.pl-3(color = "#f57e2e") mdi-plane-car
              span.pl-3 Miễn phí vận chuyển
          p.align-left Vận chuyển từ Hà Nội
          div.disacount
            p.pl-2.title-disacount.align-left Mua số lượng lớn để nhận ưu đãi
            v-checkbox.pl-2(
                label="Mua 10 sản phẩm để giảm giá"
            )
          p.align-left.pt-4 Số lượng
          fast-input-quantity.align-left(
            :value="product.quantity"
            @change-value="changeQuantity"
          )

          div(style="clear:both;")
          v-list-item.pa-0
            v-btn(color="#f57e2e" :disabled="product.quantity === 0").white--text.mt-2 Mua Hàng Ngay
            v-btn.align-left.ml-2.mt-2(:disabled="product.quantity === 0")
              span.main-color Thêm Vào Giỏ Hàng

</template>

<script>
import FastInputQuantity from '../FastInputQuantity/index.vue'

const ProductDetail = {
  props: ['screenType'],
  components: {
    FastInputQuantity
  },
  data() {
    return {
      product: {
        trademark: 'OMO',
        name: 'Nước Xả Vải Downy Nước Hoa Ngọt Ngào Dạng Chai 800ml',
        star: 4,
        sales: 1200,
        price: '1.000.000',
        cost: '1.800.000',
        quantity: 1
      }
    }
  },
  methods: {
    changeQuantity(action) {
      if (this.product.quantity === 0 && action === '-') return
      if (action === '+') this.product.quantity += 1
      if (action === '-') this.product.quantity -= 1
    }
  }
}
export default ProductDetail
</script>

<style scoped lang = "sass">
.align-left
  text-align: left
.price
  color: rgb(250,57,69)
  font-size: 30px
.disacount
  width: 400px
  border: 2px solid #f57e2e
  border-radius: 5px
.title-disacount
  font-size: 15px
.main-color
    color: #f57e2e
</style>