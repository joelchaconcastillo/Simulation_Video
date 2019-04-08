#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#define CIndividual vector<double>
#define EPS 1e-270
using namespace std;
int nvar =2;
int eta_c = 20;
int eta_c2 = 10;
double vlowBound[20];
double vuppBound[20];

ostream & operator<<(ostream &o, CIndividual a)
{
   for(int i = 0; i < a.size(); i++)
   {
	o << a[i] << " ";
   }
   return o;
}
void generateVecDouble(double a, double b, vector<double> &ind)
{
   for(int i = 0; i < nvar; i++)
     {
	double unirand = (double)(random())/RAND_MAX;
	ind[i] = a + (unirand)*(b-a);
     }
}
void real_sbx_xoverA(CIndividual &parent1, CIndividual &parent2, CIndividual &child1, CIndividual &child2)
{
    double rand;
    double y1, y2, yl, yu;
    double c1, c2;
    double alpha, beta, betaq;

                    double rr= (double)(random())/RAND_MAX;// rnd_uni(&rnd_uni_init);
        for (int i=0; i<nvar; i++)
        {
                    rand = (double)(random())/RAND_MAX;// rnd_uni(&rnd_uni_init);
            if( (double)(random())/RAND_MAX <= 1.1)
            {
                if (fabs(parent1[i]-parent2[i]) > EPS)
                {
                    if (parent1[i] < parent2[i])
                    {
                        y1 = parent1[i];
                        y2 = parent2[i];
                    }
                    else
                    {
                        y1 = parent2[i];
                        y2 = parent1[i];
                    }
                    yl = vlowBound[i];
                    yu = vuppBound[i];
                    beta = 1.0 + (2.0*(y1-yl)/(y2-y1));
                    alpha = 2.0 - pow(beta,-(eta_c+1.0));
		    //if( i == 1 )
                   // rand = (double)(random())/RAND_MAX;// rnd_uni(&rnd_uni_init);
		   // else rand == rr;
                    if (rand <= (1.0/alpha))
                    {
                        betaq = pow ((rand*alpha),(1.0/(eta_c+1.0)));
                    }
                    else
                    {
                        betaq = pow ((1.0/(2.0 - rand*alpha)),(1.0/(eta_c+1.0)));
                    }
                    c1 = 0.5*((y1+y2)-betaq*(y2-y1));
                    beta = 1.0 + (2.0*(yu-y2)/(y2-y1));
                    alpha = 2.0 - pow(beta,-(eta_c+1.0));
                    if (rand <= (1.0/alpha))
                    {
                        betaq = pow ((rand*alpha),(1.0/(eta_c+1.0)));
                    }
                    else
                    {
                        betaq = pow ((1.0/(2.0 - rand*alpha)),(1.0/(eta_c+1.0)));
                    }
                    c2 = 0.5*((y1+y2)+betaq*(y2-y1));
                    if (c1<yl)
                        c1=yl;
                    if (c2<yl)
                        c2=yl;
                    if (c1>yu)
                        c1=yu;
                    if (c2>yu)
                        c2=yu;


		if((double)random()/RAND_MAX <= 0.5  )
		{
		    if (parent1[i] < parent2[i])
                    {
      		      child1[i] = c1;
                      child2[i] = c2;
                    }
                    else
                    {
			child1[i] = c2;
                        child2[i] = c1;
                    }
		}
		else
		{

		   if (parent1[i] > parent2[i])
                    {
      		      child1[i] = c1;
                      child2[i] = c2;
                    }
                    else
                    {
			child1[i] = c2;
                        child2[i] = c1;
                    }

                   // if ( (double)(random())/RAND_MAX <=0.5)
                   // {

                   //     child1[i] = c2;
                   //     child2[i] = c1;
                   // }
                   // else
                   // {
                   //  child1[i] = c1;
                   //  child2[i] = c2;
                   // }
		}
                }
                else
                {
                    child1[i] = parent1[i];
                    child2[i] = parent2[i];
                }
            }
            else
            {
                child1[i] = parent1[i];
                child2[i] = parent2[i];
            }
        }
}
void real_sbx_xoverB(CIndividual &parent1, CIndividual &parent2, CIndividual &child1, CIndividual &child2)
{
    double rand, rand2;
    double y1, y2, yl, yu;
    double c1a, c2a, c1, c2;
    double alpha, alpha2, beta, betaq, betaq2;
    
         rand2 = (double)(random())/RAND_MAX;// rnd_uni(&rnd_uni_init);
        for (int i=0; i<nvar; i++)
        {
                    rand = (double)(random())/RAND_MAX;// rnd_uni(&rnd_uni_init);
            if( (double)(random())/RAND_MAX <= 1.5)
            {
                if (fabs(parent1[i]-parent2[i]) > EPS)
                {
                    if (parent1[i] < parent2[i])
                    {
                        y1 = parent1[i];
                        y2 = parent2[i];
                    }
                    else
                    {
                        y1 = parent2[i];
                        y2 = parent1[i];
                    }
                    yl = vlowBound[i];
                    yu = vuppBound[i];
                    beta = 1.0 + (2.0*(y1-yl)/(y2-y1));
                    alpha = 2.0 - pow(beta,-(eta_c+1.0));
                    alpha2 = 2.0 - pow(beta,-(eta_c2+1.0));

                    if (rand <= (1.0/alpha))
                    {
                        betaq = pow ((rand*alpha),(1.0/(eta_c+1.0)));
                    }
                    else
                    {
                        betaq = pow ((1.0/(2.0 - rand*alpha)),(1.0/(eta_c+1.0)));
                    }
		    if (rand2 <= (1.0/alpha2))
                    {
                        betaq2 = pow ((rand2*alpha2),(1.0/(eta_c2+1.0)));
                    }
                    else
                    {
                        betaq2 = pow ((1.0/(2.0 - rand2*alpha2)),(1.0/(eta_c2+1.0)));
                    }


                    c1 = 0.5*(y1+y2)-0.25*betaq*(y2-y1) - 0.25*(betaq2*(y2-y1))  ;
                    beta = 1.0 + (2.0*(yu-y2)/(y2-y1));
                    alpha = 2.0 - pow(beta,-(eta_c+1.0));
                    alpha2 = 2.0 - pow(beta,-(eta_c2+1.0));
                    if (rand <= (1.0/alpha))
                    {
                        betaq = pow ((rand*alpha),(1.0/(eta_c+1.0)));
                    }
                    else
                    {
                        betaq = pow ((1.0/(2.0 - rand*alpha)),(1.0/(eta_c+1.0)));
                    }
		    if (rand2 <= (1.0/alpha2))
                    {
                        betaq2 = pow ((rand2*alpha2),(1.0/(eta_c2+1.0)));
                    }
                    else
                    {
                        betaq2 = pow ((1.0/(2.0 - rand2*alpha2)),(1.0/(eta_c2+1.0)));
                    }
                    c2 = 0.5*(y1+y2)+0.25*betaq*(y2-y1)+ 0.25*(betaq2*(y2-y1));
                    if (c1<yl)
                        c1=yl;
                    if (c2<yl)
                        c2=yl;
                    if (c1>yu)
                        c1=yu;
                    if (c2>yu)
                        c2=yu;

		    if (parent1[i] < parent2[i])
                    {
      		      child1[i] = c1;
                      child2[i] = c2;
                    }
                    else
                    {
			child1[i] = c2;
                        child2[i] = c1;
                    }


//                    if ( (double)(random())/RAND_MAX <=0.5)
//                    {
//
//                        child1[i] = c2;
//                        child2[i] = c1;
//                    }
//                    else
//                    {
//                     child1[i] = c1;
//                     child2[i] = c2;
//                    }
                }
                else
                {
                    child1[i] = parent1[i];
                    child2[i] = parent2[i];
                }
            }
            else
            {
                child1[i] = parent1[i];
                child2[i] = parent2[i];
            }
        }
}
int main()
{
 srand(time(NULL));
  for(int i = 0; i < nvar; i++)
  {
	vlowBound[i] = -2;
	vuppBound[i] = 2;
  }

   vector<double> p1(nvar, 0.0), p2(nvar, 0.0), c1(nvar, 0.0), c2(nvar, 0.0);

   int N = 100000;

    generateVecDouble(0,1.0, p1); 
//    cout << p1 <<endl;
     generateVecDouble(0,1.0, p2); 
    p1[0] = -1.0;
    p1[1] = -1.0;
    p1[2] = -1.0;
    p2[0] = 1.0;
    p2[1] = 1.0;
    p2[2] = 1.0;
   for(int i = 0; i < N; i++)
   {
     
     real_sbx_xoverA(p1, p2, c1, c2 );
     cout << c1 <<endl;
	cout << c2 <<endl;
   }

   return 0;
}
