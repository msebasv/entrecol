import React, {useMemo} from "react";

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler,
  } from "chart.js";
  
  import { Line } from "react-chartjs-2";

  import './index.css'
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler
  );

  const scores = [1066, 288, 553, 3711, 545, 1491, 1708, 5341, 520];
  const labels = ["Adventure", "Animation", "Children", "Comedy", "Fantasy", "Action", "Thriller", "Drama", "Mystery"];

const options = {
  fill: true,
  responsive: true,
  scales: {
    y: {
      min: 0,
    },
  },
  plugins: {
    legend: {
      display: true,
    },
  },
};
const Graph = () => {
  const data = useMemo(function () {
    return {
      datasets: [
        {
          label: "Género",
          data: scores,
          tension: 0,
          borderColor: "rgb(75, 192, 192)",
          pointRadius: 6,
          pointBackgroundColor: "rgb(75, 192, 192)",
          backgroundColor: "rgba(75, 192, 192, 0.3)",
        },
      ],
      labels,
    };
  }, []);

  return (
      <Line data={data} options={options} />
    )
}

export default Graph