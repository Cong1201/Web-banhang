<template lang="pug">
    v-carousel(:height="height")
      v-carousel-item(v-for='(image,i) in images' :key='i' :src='image' reverse-transition='fade-transition' transition='fade-transition')

</template>

<script>
const Carousel = {
    props: ['isMobile'],
    data() {
        return {
            images: [
            'https://warmgun.com/wp-content/uploads/2021/10/banner-bds.png',
            'https://mir-s3-cdn-cf.behance.net/projects/404/59053c183008103.Y3JvcCwyNTU2LDIwMDAsMjIxLDA.jpg'
            ],
            height: 250
        }
    },
    mounted() {
        const width = screen.width
        if (width <= 600) this.height = 150
        else if (width <= 900 && width > 600) this.height = 200
        else this.height = 250
    }
}
export default Carousel
</script>