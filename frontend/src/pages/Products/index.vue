<template lang="pug">
    div
       header-bar
       .max-width.center
           v-row.pt-10.hidden-sm-and-down
             v-col(cols="2")
               categories(:items="outstandCategory" title = "Nổi bật")
             v-col(cols="8")
               carousel
               h1.main-color.pt-5 Danh Sách Sản Phẩm
             v-col(cols="2")
               v-img(src="https://d1j8r0kxyu9tj8.cloudfront.net/images/1562663273OyCyS9raIe4XXr1.jpg")
           carousel.mt-3.hidden-md-and-up

           //Category for mobile
           mobile-categories.hidden-md-and-up(:items="outstandCategory" title = "Nổi bật")

           h1.main-color.hidden-md-and-up day la autoxxx

           //pc
           v-row.hidden-sm-and-down
              v-col(cols="2")
                categories(title="Danh mục" :items="categories")
              v-col(cols="10")
                 .list-product
                    sub-product.pa-2(v-for="prd in products" :product="prd")
           //mobile
           v-row.hidden-md-and-up.hidden-sm-only
              v-col(cols="6" v-for="prd in products" )
                 v-list-item.pa-0
                    sub-product(:product="prd")

           //tab
           v-row.hidden-md-and-up.hidden-xs-only
              v-col(cols="4" v-for="prd in products" )
                 v-list-item
                    sub-product(:product="prd")
</template>

<script>
import {HeaderBar,Carousel,Categories,SubProduct,MobileCategories} from "@/components";

const Products = {
    components:{
        HeaderBar,
        Carousel,
        Categories,
        SubProduct,
        MobileCategories
    },
    data () {
      return {
        outstandCategory: [
            { text: 'Giá Tốt Mỗi Ngày', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/3c/ce/96/db8c083610e45b78d8f7662f0013faa8.png.webp' },
            { text: 'Mã Giảm Giá', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/20/68/cf/6d4adbdbcd1c35b0a438a655d9a420d0.png.webp' },
            { text: 'Ưu Đãi', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/1e/27/a7/e2c0e40b6dc45a3b5b0a8e59e2536f23.png.webp' },
            { text: 'Bảo Hiểm Hàng Hóa', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/6f/d0/68/76b6c01998c3f45f70b843c390097690.png.webp' },
            { text: 'Giao Hàng', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/4d/a3/cb/c86b6e4f17138195c026437458029d67.png.webp' },
            { text: 'Siêu Hót', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/ae/72/a3/d4503c3ece932dc8c57d2d5c97cd6ffc.png.webp' },
            { text: 'Mua Trước Trả Sau', icon: 'https://salt.tikicdn.com/cache/100x100/ts/tmp/6f/4e/41/93f72f323d5b42207ab851dfa39d44fb.png.webp' },
          ],
        categories: [
            { text: 'Quần áo công sở', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/3c/ce/96/db8c083610e45b78d8f7662f0013faa8.png.webp' },
            { text: 'Quần áo mùa đông', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/20/68/cf/6d4adbdbcd1c35b0a438a655d9a420d0.png.webp' },
            { text: 'Quần áo hot', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/1e/27/a7/e2c0e40b6dc45a3b5b0a8e59e2536f23.png.webp' },
            { text: 'Quần áo bảo hộ', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/6f/d0/68/76b6c01998c3f45f70b843c390097690.png.webp' },
            { text: 'Quần áo sinh viên', icon: 'https://salt.tikicdn.com/cache/100x100/ts/upload/4d/a3/cb/c86b6e4f17138195c026437458029d67.png.webp' }
          ],
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
          ]
      }
    }
}

export default Products
</script>

<style scoped lang="sass">
.max-width
    max-width: 1500px
.center
    margin: 0 auto
    text-align: center
.main-color
    color: #f57e2e
</style>