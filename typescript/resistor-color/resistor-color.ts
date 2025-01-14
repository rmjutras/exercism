export const colorCode = (colour?: string) => {
  enum Color {
    'black'= 0,
    'brown' = 1,
    'red' = 2,
    'orange' = 3,
    'yellow' = 4,
    'green' = 5,
    'blue' = 6,
    'violet' = 7,
    'grey' = 8,
    'white' = 9,
  }
  if (colour) {
    return Color[<any>colour];
  }

}

export const COLORS = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white'
]
