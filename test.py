import React, { useEffect, useState } from "react";
import axios from "axios";

const PodList = ({ iapValue, deployment }) => {
  const [pods, setPods] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!iapValue || !deployment) return;

    const fetchPods = async () => {
      try {
        const response = await axios.get(
          `/api/pods/${encodeURIComponent(iapValue)}/${encodeURIComponent(deployment)}`
        );
        setPods(response.data);
      } catch (err) {
        setError("Failed to fetch pods");
      } finally {
        setLoading(false);
      }
    };

    fetchPods();
  }, [iapValue, deployment]);

  if (loading) return <p>Loading pods...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h3>Pods List</h3>
      <ul>
        {pods.map((pod, index) => (
          <li key={index}>{pod}</li>
        ))}
      </ul>
    </div>
  );
};

export default PodList;
