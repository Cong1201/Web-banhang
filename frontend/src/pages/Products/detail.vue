<template lang = "pug">
  div
    header-bar
    .max-width.center
      product-detail.max-width.center.pt-10(:screen-type='screenType')
      v-divider.mt-5
      h1.main-color.text-center Sản Phẩm Tương Tự
      .list-product
        v-btn.mt-10(icon @click = "onScrollx('prev')")
          v-icon(x-large) mdi-skip-previous-circle-outline
        .list-product-content(ref = "listProduct")
          sub-product.pa-2(v-for="prd in products" :product="prd")
        v-btn.mt-10(icon @click = "onScrollx('next')")
          v-icon(x-large) mdi-skip-next-circle-outline

</template>

<script>
import {HeaderBar,ProductDetail,SubProduct} from '@/components'

const Detail = {
    components:{
      HeaderBar,
      ProductDetail,
      SubProduct
    },
    methods: {
      onScrollx(action) {
        let pos = this.$refs.listProduct.scrollLeft
        if (pos < 0) return
        if (action === 'prev') pos -= 300
        if (action === 'next') pos += 300
        this.$refs.listProduct.scroll({left: pos, behavior: 'smooth'})
      }
    },
    data() {
      return {
        screenType: 'pc',
        products: [
            {
              img: 'https://salt.tikicdn.com/cache/280x280/media/catalog/product/3/_/3.u2566.d20161018.t160236.717423.jpg.webp',
              name: 'Tủ lạnh ô tô Kemin K20 - 20L chính hãng',
              star: 5,
              sales: 1000,
              price: '1.000.000',
              cmt: 'Tặng tới 467 ASA (106K đ)',
              shipCmt: 'Giao tất cà các ngày trong tuần'
            },
            {
              img: 'https://salt.tikicdn.com/cache/280x280/ts/product/d9/b4/be/43148ac76c9471c8eaa6731df0819e9d.jpg.webp',
              name: 'Tủ lạnh ô tô Kemin K20 - 20L chính hãng',
              star: 4,
              sales: 1300,
              price: '1.700.000',
              cmt: 'Tặng tới 467 ASA (106K đ)',
              shipCmt: 'Giao tất cà các ngày trong tuần'
            },
            {
              img: 'https://salt.tikicdn.com/cache/280x280/media/catalog/product/1/_/1.u2409.d20170526.t182044.38597.jpg.webp',
              name: 'Tủ lạnh ô tô Kemin K20 - 20L chính hãng',
              star: 3,
              sales: 1500,
              price: '1.200.000',
              cmt: 'Tặng tới 467 ASA (106K đ)',
              shipCmt: 'Giao tất cà các ngày trong tuần'
            },
            {
              img: 'https://salt.tikicdn.com/cache/280x280/media/catalog/product/1/2/1225978029481.u2566.d20161018.t155948.644959.jpg.webp',
              name: 'Tủ lạnh ô tô Kemin K20 - 20L chính hãng',
              star: 3,
              sales: 1500,
              price: '1.200.000',
              cmt: 'Tặng tới 467 ASA (106K đ)',
              shipCmt: 'Giao tất cà các ngày trong tuần'
            },
            {
              img: 'https://salt.tikicdn.com/cache/280x280/media/catalog/product/3/_/3.u2566.d20161018.t160236.717423.jpg.webp',
              name: 'Tủ lạnh ô tô Kemin K20 - 20L chính hãng',
              star: 5,
              sales: 1000,
              price: '1.000.000',
              cmt: 'Tặng tới 467 ASA (106K đ)',
              shipCmt: 'Giao tất cà các ngày trong tuần'
            },
            {
              img: 'https://salt.tikicdn.com/cache/280x280/ts/product/d9/b4/be/43148ac76c9471c8eaa6731df0819e9d.jpg.webp',
              name: 'Tủ lạnh ô tô Kemin K20 - 20L chính hãng',
              star: 4,
              sales: 1300,
              price: '1.700.000',
              cmt: 'Tặng tới 467 ASA (106K đ)',
              shipCmt: 'Giao tất cà các ngày trong tuần'
            },
            {
              img: 'https://salt.tikicdn.com/cache/280x280/media/catalog/product/1/_/1.u2409.d20170526.t182044.38597.jpg.webp',
              name: 'Tủ lạnh ô tô Kemin K20 - 20L chính hãng',
              star: 3,
              sales: 1500,
              price: '1.200.000',
              cmt: 'Tặng tới 467 ASA (106K đ)',
              shipCmt: 'Giao tất cà các ngày trong tuần'
            },
            {
              img: 'https://salt.tikicdn.com/cache/280x280/media/catalog/product/1/2/1225978029481.u2566.d20161018.t155948.644959.jpg.webp',
              name: 'Tủ lạnh ô tô Kemin K20 - 20L chính hãng',
              star: 3,
              sales: 1500,
              price: '1.200.000',
              cmt: 'Tặng tới 467 ASA (106K đ)',
              shipCmt: 'Giao tất cà các ngày trong tuần'
            }
          ]
      }
    },
    mounted() {
        const widthScreen = screen.width
        if (widthScreen > 1000) this.screenType = 'pc'
        else if (widthScreen > 600) this.screenType = 'tab'
        else this.screenType = 'mobile'
      }
}
export default Detail
</script>

<style scoped lang = "sass">
.max-width
    max-width: 1500px
.center
    margin: 0 auto
    text-align: center
.main-color
    color: #f57e2e
.list-product
    display: flex
    overflow-x: auto
    box-sizing: border-box
.list-product-content
    width: 90%
    margin: 0 auto
    display: flex
    overflow-x: auto
    box-sizing: border-box
.list-product-content::-webkit-scrollbar
    width: 0

</style>