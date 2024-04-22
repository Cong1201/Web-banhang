<template lang="pug">
    div
        .header-color
            v-list-item.pa-3.max-width.center
               v-img.hidden-sm-and-down(
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQa-13lTZetsCYo-7eMOk4QlM2tPlvOf6BA2PNJSuOCXg&s"
                    max-width="40"
               )
               v-spacer
               v-text-field.pa-0(
                    label="Search"
                    placeholder="product"
                    outlined
                    hide-details
                    background-color="white"
                    height="40"
                    prepend-inner-icon="mdi-home-search-outline"
               )
               v-spacer
               div.pa-2
                 v-icon(color="white" ) mdi-home
                 span.white--text.hidden-sm-and-down Trang chủ
               div.pa-2
                 v-icon(color="white" ) mdi-account
                 span.white--text.hidden-sm-and-down Tài khoản
               div
                 v-btn(icon)
                   v-icon(color="white" ) mdi-cart-outline
               div.hidden-md-and-up
                 v-btn(icon @click="isShowCategoryInMobile = !isShowCategoryInMobile")
                   v-icon(color="white" ) mdi-menu

            v-divider(color="white")
            .pc.category.max-width.center.hidden-md-and-down
               ul
                   li.pa-2.white--text(v-for="categoryTop in categoriesTop" @click="gotoProductsPage(categoryTop)")
                        span {{ categoryTop.name }}
            .center.hidden-md-and-up
               v-expand-transition
                   v-card(
                      color="#f57e2e"
                      v-show="isShowCategoryInMobile"
                      class="mx-auto"
                   )
                      ul
                          li.pa-2.white--text(v-for="categoryTop in categoriesTop" @click="gotoProductsPage(categoryTop)")
                               span {{ categoryTop }}
</template>

<script>
import router from "@/router";
import axios from 'axios';
const HeaderBar = {
    data() {
        return{
            isShowCategoryInMobile: false,
            categoriesTop: ['Trang chủ','Nổi bật','Giảm giá','Bán chạy','Sản phẩm mới','Sản phẩm theo hãng']
        }
    },
    methods: {
        gotoProductsPage({catName}) {
            if(catName === this.categoriesTop[0]) router.push({path: '/home'})
            else router.push({path: '/products'})
        },
        async getCategory () {
          try {
            const {data} = await axios.get('http://127.0.0.1:8000/category')
            this.categoriesTop = [{name: 'Trang chủ', id: 0}].concat(data.filter(cate => cate.logo === null))
          } catch (e) {
            console.log(e)
          }
        }
    },
    mounted() {
      this.getCategory()
    }
}

export default HeaderBar
</script>

<style scoped lang="sass">
.header-color
    background-color: #f57e2e
.max-width
    max-width: 1500px
.center
    margin: 0 auto
    text-align: center
ul
    justify-content: center
    padding: 0
ul li
    text-align: center
    list-style: none
    margin: 0 3px
.pc ul li
    display: inline-block
ul li:hover
    background-color: #faabcd
    cursor: pointer
.category
    height: 40px
</style>