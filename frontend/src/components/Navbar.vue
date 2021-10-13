<template>
  <nav id="navbar">
      <router-link to="/">
        <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
            width="80px" height="70px" viewBox="0 0 212.000000 199.000000"
            preserveAspectRatio="xMidYMid meet">
            <g transform="translate(0.000000,199.000000) scale(0.100000,-0.100000)"
            fill="#ffffff" stroke="none">
                <path d="M 1130 1558 L 1130 1215 L 898 1070 C 770 990 649 915 628 902 L 590 879 L 590 1037 L 590 1196 L 720 1280 L 850 1364 L 850 1512 L 850 1660 L 625 1660 L 400 1660 L 400 1118 L 399 575 L 352 546 C 326 530 271 495 229 469 C 188 442 151 420 147 420 C 143 420 140 753 140 1160 L 140 1900 L 635 1900 L 1130 1900 L 1130 1558 Z M 1930 1045 L 1930 330 L 1780 330 L 1630 330 L 1630 676 C 1630 949 1627 1021 1618 1017 C 1611 1014 1499 946 1370 866 L 1135 719 L 1130 409 L 1125 99 L 988 192 L 851 285 L 850 576 L 850 867 L 1240 1106 L 1629 1345 L 1630 1553 L 1630 1760 L 1780 1760 L 1930 1760 L 1930 1045 Z"/>
            </g>
        </svg>
      </router-link>
      <ul v-if="user.first_name">
        <li>
          <!-- this should be a dropdown with button "sair" -->
          <p>
              {{user.first_name}}
          </p>
        </li>
      </ul>
      <a v-else href="/login">Entrar</a>
  </nav>
</template>
<script>
export default {
  props: ['user']
}
</script>
