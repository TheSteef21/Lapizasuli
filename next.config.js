/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',      // Este es el sello que crea la carpeta de salida
  trailingSlash: true,   // Esto asegura que tus links no se rompan en IPFS
  distDir: '0x41',       // Aquí le decimos que la carpeta se llame como tu ley
  images: {
    unoptimized: true,   // Vital para que las imágenes se vean en el IPFS
  },
}

module.exports = nextConfig
