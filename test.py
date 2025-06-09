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

