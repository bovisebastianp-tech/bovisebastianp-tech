<img src="assets/hero.gif" width="100%" alt="Gandesblood Tian, Frontend Developer dan UI/UX Enthusiast. Malam hujan hitam putih dengan lampu jalan dan riak genangan." />

<p align="center">
  <a href="#tentang"><img src="assets/nav-tentang.svg" height="36" alt="01 Tentang" /></a>
  <a href="#keahlian"><img src="assets/nav-keahlian.svg" height="36" alt="02 Keahlian" /></a>
  <a href="#proyek"><img src="assets/nav-proyek.svg" height="36" alt="03 Proyek" /></a>
  <a href="#perjalanan"><img src="assets/nav-perjalanan.svg" height="36" alt="04 Perjalanan" /></a>
  <a href="#prinsip"><img src="assets/nav-prinsip.svg" height="36" alt="05 Prinsip" /></a>
  <a href="#aktivitas"><img src="assets/nav-aktivitas.svg" height="36" alt="06 Aktivitas" /></a>
  <a href="#kontak"><img src="assets/nav-kontak.svg" height="36" alt="07 Kontak" /></a>
</p>

<br/>

<a id="tentang"></a>
<img src="assets/sec-tentang.svg" width="100%" alt="01 Tentang" />
<img src="assets/tentang.gif" width="100%" alt="Mahasiswa Sistem Informasi yang tertarik pada frontend development dan desain UI/UX. Menyukai dark mode, animasi yang halus, serta detail dan kerapian layout. Kelemahan: pixel geser 1px, dan itu wajib dibenerin." />

Mahasiswa Sistem Informasi yang tertarik pada **frontend development** dan **desain UI/UX**. Suka dark mode, animasi yang halus, dan layout yang rapi, dengan perhatian ke detail kecil (termasuk pixel yang geser 1px).

<br/>

<a id="keahlian"></a>
<img src="assets/sec-keahlian.svg" width="100%" alt="02 Keahlian" />
<img src="assets/keahlian.gif" width="100%" alt="Tech stack: HTML untuk struktur dan semantik halaman, CSS untuk layout, warna dan tampilan responsif, JavaScript untuk interaksi dan logika di browser, UI/UX Design untuk merancang tampilan dan alur pengguna." />

| Teknologi | Fungsi | Dipakai di |
| --- | --- | --- |
| HTML | Struktur dan semantik halaman web | Cahaya Dakwah, SIPENIL |
| CSS | Layout, warna, dan tampilan responsif | Cahaya Dakwah, SIPENIL |
| JavaScript | Interaksi dan logika di sisi browser | SIPENIL (kalkulasi nilai), Cahaya Dakwah (pemutar kajian) |
| UI/UX Design | Merancang tampilan dan alur pengguna | Antarmuka kedua proyek di atas |

<details>
<summary><b>Intip jurus gue</b> &nbsp;·&nbsp; bikin hujan pakai CSS, klik buat buka</summary>

<br/>

**CSS: tetes hujan jatuh pelan, dan berhenti buat yang gak suka animasi**

```css
.hujan {
  position: relative;
  overflow: hidden;
  background: #0a0a0b;
}

.hujan i {
  position: absolute;
  top: -10%;
  width: 1px;
  height: 60px;
  background: linear-gradient(transparent, #f4f4f2);
  animation: jatuh 1.8s linear infinite;
}

@keyframes jatuh {
  to { transform: translateY(120vh); }
}

@media (prefers-reduced-motion: reduce) {
  .hujan i { animation: none; }
}
```

**JavaScript: sebar tetesnya biar acak**

```js
document.querySelectorAll(".hujan i").forEach((tetes) => {
  tetes.style.left = Math.random() * 100 + "%";
  tetes.style.animationDelay = Math.random() * 2 + "s";
});
```

</details>

<br/>

<a id="proyek"></a>
<img src="assets/sec-proyek.svg" width="100%" alt="03 Proyek" />

<img src="assets/proyek-dakwah.gif" width="100%" alt="Cahaya Dakwah (web-dakwah): prototipe web dakwah digital dengan lima halaman, yaitu Beranda, Kajian, Artikel, Donasi, dan Putar Kajian. Tujuan: latihan merancang situs multi-halaman yang bersih dan responsif. Teknologi: HTML, CSS, JavaScript." />

**Cahaya Dakwah** · [Live Demo](https://bovisebastianp-tech.github.io/web-dakwah/) · [Source Code](https://github.com/bovisebastianp-tech/web-dakwah)

<details>
<summary>Yang ada di dalamnya</summary>

- Lima halaman: Beranda, Kajian, Artikel, Donasi, dan Putar Kajian.
- Artikel dengan filter kategori dan tombol simpan bacaan.
- Donasi dengan pilihan nominal dan kolom nominal lain.
- Statusnya prototipe.

</details>

<img src="assets/proyek-sipenil.gif" width="100%" alt="SIPENIL (web-SIPENIL): Sistem Informasi Pengelolaan dan Kalkulasi Nilai Mahasiswa dengan peran admin, dosen, dan mahasiswa. Tujuan: mengelola nilai dan menghitung hasil studi mahasiswa Prodi Sistem Informasi. Teknologi: HTML, CSS, JavaScript." />

**SIPENIL** · [Live Demo](https://bovisebastianp-tech.github.io/web-SIPENIL/) · [Source Code](https://github.com/bovisebastianp-tech/web-SIPENIL)

<details>
<summary>Yang ada di dalamnya</summary>

- Tiga peran pengguna: admin, dosen, dan mahasiswa.
- Admin mengelola data mahasiswa, dosen, dan mata kuliah, serta bisa mencetak KHS.
- Bobot nilai bisa diatur dan disimpan.

</details>

<img src="assets/proyek-berikutnya.gif" width="100%" alt="Proyek berikutnya. Masih jadi bibit, belum tumbuh ke permukaan. Segera." />

<br/>

<a id="perjalanan"></a>
<img src="assets/sec-perjalanan.svg" width="100%" alt="04 Perjalanan belajar" />
<img src="assets/jalur-belajar.gif" width="100%" alt="Perjalanan belajar: HTML, CSS, JavaScript, UI/UX, lalu proyek yang lebih kompleks yang belum sampai." />

<br/>

<a id="prinsip"></a>
<img src="assets/sec-prinsip.svg" width="100%" alt="05 Prinsip kerja" />
<img src="assets/prinsip.gif" width="100%" alt="Prinsip kerja: pixel geser 1px wajib dibenerin, dark mode itu kebutuhan, animasi harus halus bukan bikin pusing, layout bersih lebih penting dari basa-basi. Bangun pagi: belum, dan gak akan." />

<br/>

<a id="aktivitas"></a>
<img src="assets/sec-aktivitas.svg" width="100%" alt="06 Aktivitas" />

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=bovisebastianp-tech&theme=dark&background=0A0A0B&border=2A2A2E&ring=F4F4F2&fire=F4F4F2&currStreakLabel=F4F4F2&sideLabels=9A9AA0&dates=5C5C62&currStreakNum=F4F4F2&sideNums=F4F4F2&stroke=2A2A2E&border_radius=0" alt="Streak kontribusi GitHub" />
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bovisebastianp-tech/bovisebastianp-tech/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/bovisebastianp-tech/bovisebastianp-tech/output/github-snake.svg" />
    <img src="https://raw.githubusercontent.com/bovisebastianp-tech/bovisebastianp-tech/output/github-snake-dark.svg" alt="Ular yang memakan grafik kontribusi GitHub" width="100%" />
  </picture>
</p>

<br/>

<a id="kontak"></a>
<img src="assets/sec-kontak.svg" width="100%" alt="07 Kontak" />
<a href="https://github.com/bovisebastianp-tech"><img src="assets/kontak.gif" width="100%" alt="Kunjungi github.com/bovisebastianp-tech." /></a>

GitHub: [github.com/bovisebastianp-tech](https://github.com/bovisebastianp-tech)

<br/>

<img src="assets/footer.gif" width="100%" alt="Ngoding? Desain ajah. Hujan di luar itu paling adem dan tenang." />
