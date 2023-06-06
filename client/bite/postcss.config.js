import tailwindcss from 'tailwindcss';
import autoprefixer from 'autoprefixer';
import purgecss from '@fullhuman/postcss-purgecss';

export default {
  plugins: [
    tailwindcss,
    autoprefixer,
    process.env.NODE_ENV === 'production' &&
      purgecss({
        content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'],
        safelist: ['bg-red-500'], // Add any classes that should not be purged
      }),
  ],
};
